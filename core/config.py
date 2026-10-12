import os

from dotenv import load_dotenv

load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} is not set")
    return value


DISCORD_TOKEN = get_required_env("DISCORD_TOKEN")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.5-flash-lite",
)
GEMINI_MAX_OUTPUT_TOKENS = int(
    os.getenv("GEMINI_MAX_OUTPUT_TOKENS", "500")
)

AI_COOLDOWN_SECONDS = int(
    os.getenv("AI_COOLDOWN_SECONDS", "5")
)
MAX_MEMORY_MESSAGES = int(
    os.getenv("MAX_MEMORY_MESSAGES", "10")
)
MAX_MEMORY_CHARS = int(
    os.getenv("MAX_MEMORY_CHARS", "4000")
)
