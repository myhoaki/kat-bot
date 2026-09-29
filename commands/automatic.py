import re

import discord
from discord.ext import commands

from core.ai import (
    can_use_ai,
    get_ai_reply,
    mark_ai_used,
)
from core.auto_reactions import get_reaction


class AutomaticReactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.startswith("?kat"):
            return

        # --------------------------------------------------
        # AI replies when Kat is directly mentioned
        # --------------------------------------------------

        if self.bot.user in message.mentions:
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

                    # Only start cooldown after success.
                    mark_ai_used(
                        message.author.id
                    )

                except discord.HTTPException as exc:
                    print(
                        f"[AI] Failed to send AI reply: {exc}",
                        flush=True,
                    )

                    await message.channel.send(
                        "💀 I had a thought and Discord "
                        "fucked the delivery."
                    )

            else:
                await message.channel.send(
                    "💀 Kat's brain just blue-screened. "
                    "Try again in a few seconds."
                )

            return

        # --------------------------------------------------
        # Automatic keyword reactions
        # --------------------------------------------------

        reaction = get_reaction(
            message.content
        )

        if reaction:
            try:
                await message.channel.send(
                    reaction["message"]
                )

                await message.add_reaction(
                    reaction["emoji"]
                )

            except discord.Forbidden:
                print(
                    "[AUTO] Kat does not have permission "
                    "to send messages or add reactions.",
                    flush=True,
                )

            except discord.HTTPException as exc:
                print(
                    f"[AUTO] Failed to process "
                    f"automatic reaction: {exc}",
                    flush=True,
                )


async def setup(bot):
    await bot.add_cog(
        AutomaticReactions(bot)
    )