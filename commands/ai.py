import re

import discord
from discord.ext import commands

from core.ai import (
    can_use_ai,
    get_ai_reply,
    mark_ai_used,
)


class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.startswith("?kat"):
            return

        if self.bot.user not in message.mentions:
            return

        if not can_use_ai(message.author.id):
            await message.reply(
                "Give me a fucking second. 💀",
                mention_author=False,
            )
            return

        user_message = re.sub(
            rf"<@!?{self.bot.user.id}>",
            "",
            message.content,
        ).strip()

        if not user_message:
            user_message = (
                "Someone just mentioned me. "
                "Say something funny."
            )

        reply = None

        try:
            async with message.channel.typing():
                reply = await self.bot.loop.run_in_executor(
                    None,
                    get_ai_reply,
                    user_message,
                    message.channel.id,
                    message.author.display_name,
                )

        except Exception as exc:
            print(
                f"[AI] Unexpected Discord AI error: {exc}",
                flush=True,
            )

        if reply:
            try:
                await message.reply(
                    reply,
                    mention_author=False,
                )

                mark_ai_used(message.author.id)

            except discord.HTTPException as exc:
                print(
                    f"[AI] Failed to send AI reply: {exc}",
                    flush=True,
                )

                await message.channel.send(
                    "I had a thought and Discord fucked the delivery."
                )

        else:
            await message.channel.send(
                "Kat's brain just blue-screened. "
                "Try again in a few seconds."
            )


async def setup(bot):
    await bot.add_cog(AI(bot))
