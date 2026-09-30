import os
import tempfile

import discord
from discord.ext import commands

from core.tts import generate_tts, translate_text


class TTSCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, text: str):
        """Generate speech with Gemini and send it as an audio file."""

        if len(text) > 500:
            await ctx.send("Keep it under 500 characters.")
            return

        await ctx.send("Generating audio...")
        use_japanese = text.lower().endswith("-jp")

        if use_japanese:
            text = text[:-3].rstrip()
            text = await self.bot.loop.run_in_executor(
                None,
                translate_text,
                text,
            )
        output_path = tempfile.mktemp(suffix=".wav")

        try:
            await self.bot.loop.run_in_executor(
                None,
                generate_tts,
                text,
                output_path,
            )

            await ctx.send(
                file=discord.File(output_path, filename="kat-tts.wav")
            )

        except Exception as exc:
            print(f"[TTS] Error: {exc}", flush=True)
            await ctx.send("TTS failed. All configured Gemini keys/models may be unavailable.")

        finally:
            if os.path.exists(output_path):
                os.remove(output_path)


async def setup(bot):
    await bot.add_cog(TTSCommands(bot))
