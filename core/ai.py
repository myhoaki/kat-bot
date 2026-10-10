import os
import time

from google import genai
from google.genai import types

from core.aipersonalities import get_system_prompt


AI_COOLDOWN_SECONDS = 5

last_ai_reply = {}

# Lightweight in-memory conversation history.
# Key: Discord channel ID
# Value: list of recent "username: message" strings
conversation_memory = {}

MAX_MEMORY_MESSAGES = 10
MAX_MEMORY_CHARS = 4000




def can_use_ai(user_id: int) -> bool:
    now = time.monotonic()

    last_used = last_ai_reply.get(
        user_id,
        0,
    )

    return (
        now - last_used
        >= AI_COOLDOWN_SECONDS
    )


def mark_ai_used(user_id: int):
    last_ai_reply[user_id] = time.monotonic()


def get_ai_reply(
    user_message: str,
    channel_id: int | None = None,
    username: str = "User",
):
    api_key = os.getenv(
        "GEMINI_API_KEY"
    )

    if not api_key:
        print(
            "[AI] GEMINI_API_KEY is not configured.",
            flush=True,
        )
        return None

    # Build a small rolling conversation history.
    history = []

    if channel_id is not None:
        history = conversation_memory.get(
            channel_id,
            [],
        )

    current_message = f"{username}: {user_message}"

    if history:
        contents = (
            "Recent conversation:\n"
            + "\n".join(history)
            + "\n\n"
            + "Current message:\n"
            + current_message
        )
    else:
        contents = current_message

    try:
        client = genai.Client(
            api_key=api_key
        )

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=get_system_prompt(),
                max_output_tokens=500,
            ),
        )

        reply = response.text

    except Exception as exc:
        error = str(exc)

        if (
            "429" in error
            or "RESOURCE_EXHAUSTED" in error
            or "quota" in error.lower()
        ):
            print(
                "[AI] Gemini quota/rate limit reached.",
                flush=True,
            )
        else:
            print(
                f"[AI] Gemini request failed: {exc}",
                flush=True,
            )

        return None

    if not isinstance(reply, str):
        print(
            "[AI] Gemini returned a non-text response.",
            flush=True,
        )
        return None

    reply = reply.strip()

    if not reply:
        print(
            "[AI] Gemini returned an empty response.",
            flush=True,
        )
        return None

    # Only remember successful conversations.
    if channel_id is not None:
        memory = conversation_memory.setdefault(
            channel_id,
            [],
        )

        memory.append(current_message)
        memory.append(f"Kat: {reply}")

        # Keep only the most recent messages.
        del memory[:-MAX_MEMORY_MESSAGES]

        # Keep total memory small.
        while (
            sum(len(item) for item in memory)
            > MAX_MEMORY_CHARS
            and len(memory) > 1
        ):
            memory.pop(0)

    return reply
