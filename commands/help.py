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
            description=(
                "What are you up to?\n\n"
                "🐱 Kat is watching. Choose wisely."
            ),
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
                "`?kat preg @member`\n\n"
                "Kat will respond with a random reaction "
                "and GIF."
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
            name="🎭 Kat's Personality",
            value=(
                "`?kat mood`\n"
                "`?kat roast @user`\n"
                "`?kat compliment @user`\n"
                "`?kat judge @user`\n"
                "`?kat wisdom`\n"
                "`?kat chaos`"
            ),
            inline=False,
        )

        embed.add_field(
            name="🎮 Games",
            value=(
                "`?kat coinflip`\n"
                "`?kat 8ball <question>`\n"
                "`?kat roll [count] [sides]`\n\n"
                "Roll up to 10 dice with up to 100 sides."
            ),
            inline=False,
        )

        embed.add_field(
            name="🎞️ GIFs",
            value=(
                "`?kat gifs`\n"
                "`?kat gifs <action>`\n\n"
                "See available GIF categories and the GIFs "
                "currently loaded for each action."
            ),
            inline=False,
        )

        embed.add_field(
            name="🛠️ GIF Management",
            value=(
                "`?kat addgif <action>`\n"
                "`?kat removegif <action> <number>`\n\n"
                "Attach a `.gif` when using `addgif`.\n"
                "Manage Server permission is required.\n"
                "New GIFs are automatically numbered like "
                "`hug001.gif`, `hug002.gif`, etc.\n"
                "Removed numbers can be reused automatically."
            ),
            inline=False,
        )

        embed.add_field(
            name="<:giga_mpreg:1512315959279353986> Automatic Reactions",
            value=(
                "Kat may randomly react to certain words "
                "or phrases in normal conversation. 👀\n\n"
            ),
            inline=False,
        )

        embed.add_field(
            name="⚙️ Other",
            value="`?kat help`",
            inline=False,
        )

        embed.set_footer(
            text="Kat Bot • Behave yourself. Or don't. 💀"
        )

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(
        HelpCommands(bot)
    )