from discord.ext import commands

from core.aipersonalities import (
    PERSONALITIES,
    get_personality,
    set_personality,
)


class AIPersonality(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="personality")
    async def personality(self, ctx, name: str | None = None):
        """View or change Kat's global AI personality."""

        if name is None:
            current = get_personality()
            available = ", ".join(sorted(PERSONALITIES))

            await ctx.send(
                f"Current AI personality: `{current}`\n"
                f"Available: `{available}`"
            )
            return

        if not set_personality(name):
            available = ", ".join(sorted(PERSONALITIES))

            await ctx.send(
                f"Unknown AI personality `{name}`.\n"
                f"Available: `{available}`"
            )
            return

        await ctx.send(
            f"AI personality changed to `{get_personality()}`."
        )


async def setup(bot):
    await bot.add_cog(AIPersonality(bot))
