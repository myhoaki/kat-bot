import discord
from discord.ext import commands

from core.personality import (
    random_chaos,
    random_compliment,
    random_judgment,
    random_mood,
    random_roast,
    random_wisdom,
)


class PersonalityCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mood(self, ctx):
        await ctx.send(
            f"🐱 I'm feeling **{random_mood()}**."
        )

    @commands.command()
    async def roast(
        self,
        ctx,
        member: discord.Member,
    ):
        await ctx.send(
            random_roast(member)
        )

    @commands.command()
    async def compliment(
        self,
        ctx,
        member: discord.Member,
    ):
        await ctx.send(
            random_compliment(member)
        )

    @commands.command()
    async def judge(
        self,
        ctx,
        member: discord.Member,
    ):
        await ctx.send(
            f"{random_judgment()}"
        )

    @commands.command()
    async def wisdom(self, ctx):
        await ctx.send(
            random_wisdom()
        )

    @commands.command()
    async def chaos(self, ctx):
        await ctx.send(
            random_chaos()
        )


async def setup(bot):
    await bot.add_cog(
        PersonalityCommands(bot)
    )