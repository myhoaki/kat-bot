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

- Python 3.12 or newer
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

Kat-Bot uses environment variables for API credentials and other configuration.

Create a `.env` file in the project directory.

Example:

```env
DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

**Never commit `.env` to Git.**

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

## Project Structure

```text
kat-bot/
├── bot.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── commands/
│   ├── __init__.py
│   ├── actions.py
│   ├── aipersonality.py
│   ├── ai.py
│   ├── games.py
│   ├── gifs.py
│   └── help.py
│
├── core/
│   ├── __init__.py
│   ├── actions.py
│   ├── ai.py
│   └── aipersonalities.py
│
├── gifs/
│   └── ...
│
└── data/
    └── ...
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

Check the Git working tree:

```bash
git status
```

## License

This project is intended for personal and private self-hosting.

## About

Kat-Bot is a small Discord bot built for a private community.

> A small Discord bot built to cause a reasonable amount of chaos.
