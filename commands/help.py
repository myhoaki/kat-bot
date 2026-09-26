import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(
            title=(
                "<:giga_mpreg:1512315959279353986>"
                " Kat Bot Commands "
                "<:giga_mpreg:1512315959279353986>"
            ),
            description="What are you up to?",
            color=discord.Color.blurple(),
        )

        embed.add_field(
            name="🐾 Interactions",
            value=(
                "`?kat hug @member`\n"
                "`?kat kiss @member`\n"
                "`?kat pat @member`\n"
                "`?kat slap @member`\n"
                "`?kat cuddle @member`\n"
                "`?kat highfive @member`\n"
                "`?kat preg @member`"
            ),
            inline=False,
        )

        embed.add_field(
            name="💕 Relationships",
            value=(
                "`?kat ship @user1 @user2`\n"
                "`?kat relationship @user1 @user2`\n"
                "`?kat friendship @user`"
            ),
            inline=False,
        )

        embed.add_field(
            name="🎮 Games",
            value=(
                "`?kat coinflip`\n"
                "`?kat 8ball <question>`\n"
                "`?kat roll [count] [sides]`"
            ),
            inline=False,
        )

        embed.add_field(
            name="⚙️ Other",
            value="`?kat help`",
            inline=False,
        )

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(
        HelpCommands(bot)
    )