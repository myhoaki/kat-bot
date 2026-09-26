import discord
from discord.ext import commands

from core.actions import send_action


class ActionCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(
        self,
        ctx,
        member: discord.Member,
    ):
        await send_action(
            ctx,
            member,
            "hug",
            f"hugs {member.mention}! 🫂",
        )

    @commands.command()
    async def kiss(
        self,
        ctx,
        member: discord.Member,
    ):
        await send_action(
            ctx,
            member,
            "kiss",
            f"kisses {member.mention}! 💋",
        )

    @commands.command()
    async def pat(
        self,
        ctx,
        member: discord.Member,
    ):
        await send_action(
            ctx,
            member,
            "pat",
            f"pats {member.mention}! 🥰",
        )

    @commands.command()
    async def slap(
        self,
        ctx,
        member: discord.Member,
    ):
        await send_action(
            ctx,
            member,
            "slap",
            f"slaps {member.mention}! 👋",
        )

    @commands.command()
    async def cuddle(
        self,
        ctx,
        member: discord.Member,
    ):
        await send_action(
            ctx,
            member,
            "cuddle",
            f"cuddles {member.mention}! 🤗",
        )

    @commands.command()
    async def highfive(
        self,
        ctx,
        member: discord.Member,
    ):
        await send_action(
            ctx,
            member,
            "highfive",
            f"high-fives {member.mention}! 🙌",
        )

    @commands.command()
    async def preg(
        self,
        ctx,
        member: discord.Member,
    ):
        await send_action(
            ctx,
            member,
            "preg",
            f"pregs {member.mention}! "
            "<:giga_mpreg:1512315959279353986>",
        )


async def setup(bot):
    await bot.add_cog(ActionCommands(bot))