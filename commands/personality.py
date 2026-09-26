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
        embed = discord.Embed(
            title="🐱 Kat's Current Mood",
            description=(
                f"Kat is currently feeling "
                f"**{random_mood()}**."
            ),
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def roast(
        self,
        ctx,
        member: discord.Member,
    ):
        await ctx.send(
            f"🔥 **Kat's Roast Department**\n"
            f"{random_roast(member)}"
        )

    @commands.command()
    async def compliment(
        self,
        ctx,
        member: discord.Member,
    ):
        await ctx.send(
            f"❤️ **Kat Has Something Nice To Say**\n"
            f"{random_compliment(member)}"
        )

    @commands.command()
    async def judge(
        self,
        ctx,
        member: discord.Member,
    ):
        await ctx.send(
            f"👩‍⚖️ **Kat's Official Judgment of "
            f"{member.display_name}**\n"
            f"{random_judgment()}"
        )

    @commands.command()
    async def wisdom(self, ctx):
        await ctx.send(
            f"🧠 **Kat's Wisdom**\n"
            f"{random_wisdom()}"
        )

    @commands.command()
    async def chaos(self, ctx):
        await ctx.send(
            f"💀 **CHAOS DEPARTMENT**\n"
            f"{random_chaos()}"
        )


async def setup(bot):
    await bot.add_cog(
        PersonalityCommands(bot)
    )