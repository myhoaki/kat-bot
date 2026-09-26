import random

from discord.ext import commands


class GameCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        result = random.choice(
            ("Heads", "Tails")
        )

        await ctx.send(
            f"🪙 **{result}!**"
        )

    @commands.command(name="8ball")
    async def eight_ball(
        self,
        ctx,
        *,
        question: str,
    ):
        answers = (
            "It is certain. ✨",
            "Without a doubt. 🔮",
            "The stars say yes! 🌟",
            "Ask again after a snack. 🍪",
            "Signs point to maybe... 👀",
            "I wouldn't count on it. 😬",
            "Absolutely not. 🙅",
        )

        await ctx.send(
            f"🎱 **{ctx.author.display_name} asks:** "
            f"{question}\n"
            f"{random.choice(answers)}"
        )

    @commands.command()
    async def roll(
        self,
        ctx,
        count: int = 1,
        sides: int = 6,
    ):
        if count < 1 or count > 10:
            await ctx.send(
                "🎲 Dice count must be "
                "**between 1 and 10**."
            )
            return

        if sides < 2 or sides > 100:
            await ctx.send(
                "🎲 Dice sides must be "
                "**between 2 and 100**."
            )
            return

        results = [
            random.randint(1, sides)
            for _ in range(count)
        ]

        total = sum(results)

        detail = " + ".join(
            str(result)
            for result in results
        )

        await ctx.send(
            f"🎲 {ctx.author.mention} rolled "
            f"**{total}** ({detail}) "
            f"on {count}d{sides}!"
        )


async def setup(bot):
    await bot.add_cog(
        GameCommands(bot)
    )