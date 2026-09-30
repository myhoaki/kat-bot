from discord.ext import commands

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

        reaction = get_reaction(message.content)

        if reaction:
            try:
                await message.channel.send(
                    reaction["message"]
                )

                await message.add_reaction(
                    reaction["emoji"]
                )

            except Exception as exc:
                print(
                    f"[AUTO] Failed to process reaction: {exc}",
                    flush=True,
                )


async def setup(bot):
    await bot.add_cog(AutomaticReactions(bot))
