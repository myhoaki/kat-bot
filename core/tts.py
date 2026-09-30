import os
import time
import wave

from google import genai
from google.genai import types
from core.aipersonalities import get_personality

TTS_MODEL = "gemini-3.8-flash-lite-tts"
TTS_FALLBACK_MODEL = "gemini-3.8-flash-tts"

PERSONALITY_VOICES = {
    "butcher": ("Algenib", "gravelly, cynical, sarcastic, rough British delivery"),
    "normal": ("Achird", "friendly, casual, natural"),
    "tsundere": ("Leda", "youthful, irritated, flustered"),
    "yandere": ("Gacrux", "calm, mature, quietly unsettling"),
    "kuudere": ("Schedar", "even, detached, monotone"),
    "dandere": ("Achird", "soft, quiet, shy"),
    "chuunibyou": ("Fenrir", "excitable, dramatic, theatrical"),
    "onee-san": ("Sulafat", "warm, confident, composed"),
    "gyaru": ("Puck", "upbeat, energetic, playful"),
}

DEFAULT_VOICE = ("Kore", "natural, conversational delivery")

def get_tts_voice():
    personality = get_personality()
    return PERSONALITY_VOICES.get(personality, DEFAULT_VOICE)


# Don't retry a key that hit a quota/rate-limit error for 5 minutes.
KEY_COOLDOWN_SECONDS = 300

key_cooldowns = {}

def translate_text(text: str, language: str = "Japanese") -> str:
    keys = get_tts_keys()

    if not keys:
        raise RuntimeError("No Gemini API keys configured.")

    last_error = None

    for key_number, key in keys:
        client = genai.Client(api_key=key)

        try:
            print(
                f"[TTS] Translating with key {key_number}",
                flush=True,
            )

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=(
                    f"Translate the following text into {language}. "
                    "Return only the translation. "
                    "Do not add explanations.\n\n"
                    f"{text}"
                ),
            )

            return response.text.strip()

        except Exception as exc:
            last_error = exc
            print(
                f"[TTS] Translation failed with key {key_number}: {exc}",
                flush=True,
            )

    raise RuntimeError(
        f"Translation failed with all available Gemini keys: {last_error}"
    )

def get_tts_keys():
    keys = []

    for i in range(1, 20):
        key = os.getenv(f"GEMINI_TTS_KEY_{i}")

        if key:
            keys.append((i, key))

    return keys


def is_quota_error(error):
    error_text = str(error).lower()

    return any(
        phrase in error_text
        for phrase in (
            "resource_exhausted",
            "quota",
            "rate limit",
            "429",
            "too many requests",
        )
    )


def generate_tts(text: str, output_path: str):
    voice_name, voice_style = get_tts_voice()

    keys = get_tts_keys()

    if not keys:
        raise RuntimeError("No Gemini TTS API keys configured.")

    last_error = None
    now = time.time()

    for key_number, key in keys:
        cooldown_until = key_cooldowns.get(key_number, 0)

        if now < cooldown_until:
            remaining = int(cooldown_until - now)

            print(
                f"[TTS] Key {key_number} is on cooldown "
                f"({remaining}s remaining).",
                flush=True,
            )
            continue

        client = genai.Client(api_key=key)

        for model in (TTS_MODEL, TTS_FALLBACK_MODEL):
            try:
                print(
                    f"[TTS] Trying key {key_number} with {model}",
                    flush=True,
                )

                response = client.models.generate_content(
                    model=model,
                    contents=[{
                        "role": "user",
                        "parts": [{
                            "text": text,
                            "speech_metadata": {
                                "style": voice_style,
                            },
                        }],
                    }],
                    config=types.GenerateContentConfig(
                        response_modalities=["AUDIO"],

                        speech_config=types.SpeechConfig(
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=voice_name,
                                )
                            )
                        ),
                    ),
                )

                audio = response.candidates[0].content.parts[0].inline_data.data

                with wave.open(output_path, "wb") as wav:
                    wav.setnchannels(1)
                    wav.setsampwidth(2)
                    wav.setframerate(24000)
                    wav.writeframes(audio)

                print(
                    f"[TTS] Success with key {key_number} / {model}",
                    flush=True,
                )

                return output_path

            except Exception as exc:
                last_error = exc

                print(
                    f"[TTS] Key {key_number} / {model} failed: {exc}",
                    flush=True,
                )

                if is_quota_error(exc):
                    key_cooldowns[key_number] = (
                        time.time() + KEY_COOLDOWN_SECONDS
                    )

                    print(
                        f"[TTS] Key {key_number} hit quota/rate limit. "
                        f"Cooling down for {KEY_COOLDOWN_SECONDS}s.",
                        flush=True,
                    )

                    break

    raise RuntimeError(
        f"All available Gemini TTS keys/models failed: {last_error}"
    )