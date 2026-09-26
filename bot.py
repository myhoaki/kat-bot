import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="?kat ",
    intents=intents,
    help_command=None,
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}", flush=True)
    print("kat-bot is online!", flush=True)
    print("Prefix: ?kat", flush=True)


async def load_extensions():
    extensions = (
        "commands.actions",
        "commands.games",
        "commands.relationships",
        "commands.help",
        "commands.personality",
    )

    for extension in extensions:
        await bot.load_extension(extension)
        print(f"Loaded: {extension}", flush=True)

async def main():
    if not TOKEN:
        raise RuntimeError(
            "DISCORD_TOKEN is not set in .env"
        )

    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


import asyncio

asyncio.run(main())
