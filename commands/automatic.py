import discord
from discord.ext import commands

from core.auto_reactions import get_reaction


class AutomaticReactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore bots.
        if message.author.bot:
            return

        # Don't automatically react to commands.
        if message.content.startswith("?kat"):
            return

        reaction = get_reaction(message.content)

        if reaction:
            try:
                # Send Kat's response.
                await message.channel.send(
                    reaction["message"]
                )

                # Add the emoji reaction to the
                # message that triggered Kat.
                await message.add_reaction(
                    reaction["emoji"]
                )

            except discord.Forbidden:
                print(
                    "Kat does not have permission "
                    "to send messages or add reactions.",
                    flush=True,
                )

            except discord.HTTPException as exc:
                print(
                    f"Failed to process automatic reaction: {exc}",
                    flush=True,
                )


async def setup(bot):
    await bot.add_cog(
        AutomaticReactions(bot)
    )