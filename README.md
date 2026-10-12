# Kat-Bot

A small, self-hosted Discord bot built for a private Discord community.

Kat-Bot combines custom Discord commands, AI personalities, GIF interactions, games, and utility commands into one modular bot.

## Features

- Custom Discord commands
- Multiple AI personalities
- Personality-aware AI responses
- GIF-based interactions
- Games and utility commands
- Modular command system
- Docker and Docker Compose support
- Local data storage

## Commands

### Interactions

```text
?kat hug @member
?kat kiss @member
?kat pat @member
?kat slap @member
?kat cuddle @member
?kat highfive @member
?kat preg @member
```

### Games

```text
?kat coinflip
?kat 8ball <question>
?kat roll [count] [sides]
```

`<required>` arguments must be provided.

`[optional]` arguments can be omitted.

### AI

Mention Kat and send a message to get an AI response.

View the current personality:

```text
?kat personality
```

Change the personality:

```text
?kat personality <name>
```

Available personalities:

```text
butcher
chuunibyou
dandere
gyaru
kuudere
normal
onee-san
tsundere
yandere
```

### GIFs

View available GIFs:

```text
?kat gifs
```

View GIFs for a specific action:

```text
?kat gifs <action>
```

Add a GIF:

```text
?kat addgif <action>
```

Remove a GIF:

```text
?kat removegif <action> <number>
```

## Requirements

Before installing Kat-Bot, make sure you have:

- Python 3.12 or newer (for running outside Docker)
- Docker
- Docker Compose
- A Discord bot application
- A Discord bot token
- A Google Gemini API key

## Installation

Clone the repository:

```bash
git clone https://github.com/myhoaki/kat-bot.git
cd kat-bot
```

Create the environment file:

```bash
cp .env.example .env
```

Edit the environment variables:

```bash
nano .env
```

Build and start the bot:

```bash
docker compose build
docker compose up -d
```

Check the container:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f kat-bot
```

## Configuration

Kat-Bot uses environment variables for API credentials and runtime configuration.

Create a `.env` file in the project directory using `.env.example` as a template.

Example:

```env
# Discord bot token
DISCORD_TOKEN=your_discord_bot_token

# Gemini API key for AI responses
GEMINI_API_KEY=your_gemini_api_key

# Gemini text model
GEMINI_MODEL=gemini-3.5-flash-lite

# Maximum generated response length
GEMINI_MAX_OUTPUT_TOKENS=500

# Minimum time between AI replies from the same user, in seconds
AI_COOLDOWN_SECONDS=5

# In-memory conversation history limits
MAX_MEMORY_MESSAGES=10
MAX_MEMORY_CHARS=4000
```

| Variable | Description | Default |
|---|---|---|
| `DISCORD_TOKEN` | Discord bot token; required | None |
| `GEMINI_API_KEY` | Gemini API key for AI responses | Empty |
| `GEMINI_MODEL` | Gemini text model | `gemini-3.5-flash-lite` |
| `GEMINI_MAX_OUTPUT_TOKENS` | Maximum generated response tokens | `500` |
| `AI_COOLDOWN_SECONDS` | AI response cooldown per user, in seconds | `5` |
| `MAX_MEMORY_MESSAGES` | Maximum conversation history messages | `10` |
| `MAX_MEMORY_CHARS` | Maximum conversation history characters | `4000` |

**Never commit `.env` to Git.** The `.env.example` file contains placeholders and can safely be committed.

## Docker

Kat-Bot is designed to run as a Docker Compose service.

Build the image:

```bash
docker compose build
```

Start the bot:

```bash
docker compose up -d
```

Stop the bot:

```bash
docker compose down
```

Restart the bot:

```bash
docker compose restart
```

View logs:

```bash
docker compose logs -f kat-bot
```

Rebuild after code changes:

```bash
docker compose build
docker compose up -d
```

The bot stores persistent files through Docker bind mounts:

```text
gifs/  → /app/gifs
data/  → /app/data
```

The `gifs/` directory stores GIF assets. The `data/` directory is mounted for application data.

## Project Structure

```text
kat-bot/
├── .env.example
├── .gitignore
├── Dockerfile
├── compose.yml
├── requirements.txt
├── services.yaml
├── README.md
├── bot.py
│
├── commands/
│   ├── __init__.py
│   ├── actions.py
│   ├── ai.py
│   ├── aipersonality.py
│   ├── games.py
│   ├── gifs.py
│   └── tts.py
│
├── core/
│   ├── __init__.py
│   ├── actions.py
│   ├── ai.py
│   ├── aipersonalities.py
│   ├── config.py
│   ├── reactions.py
│   ├── stickers.py
│   └── tts.py
│
├── gifs/
│   └── ...
│
└── data/
    └── ... (runtime data)
```

## AI Personalities

Kat-Bot supports several AI personalities that change how Kat responds.

The current personalities are:

- **Butcher** — rough, cynical, and sarcastic
- **Normal** — friendly and conversational
- **Tsundere** — youthful and flustered
- **Yandere** — calm and unsettling
- **Kuudere** — detached and monotone
- **Dandere** — quiet and shy
- **Chuunibyou** — dramatic and theatrical
- **Onee-san** — warm and confident
- **Gyaru** — energetic and playful

The selected personality is stored in memory and resets to the default personality when the bot restarts.

## Security

Keep your credentials private.

Do not commit API keys or Discord tokens to Git:

```text
.env
```

If a credential is accidentally exposed, revoke it and generate a replacement immediately.

## Development

Run a syntax check before rebuilding:

```bash
python -m py_compile bot.py
```

After making code changes, rebuild and restart the container:

```bash
docker compose build
docker compose up -d
```

Check the logs for errors:

```bash
docker compose logs --tail=100 kat-bot
```

## License

This project is intended for private self-hosting. Make sure you have permission to use any third-party assets, including GIFs and audio files, that you add to your own instance.

---

*A small Discord bot built to cause a reasonable amount of chaos.*
