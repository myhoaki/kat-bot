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
            description="🐱 Kat is watching. Choose wisely.",
            color=discord.Color.blurple(),
        )

        embed.add_field(
            name="🐾 Interactions",
            value=(
                "`?kat hug @member` `kiss` `pat` `slap`\n"
                "`cuddle` `highfive` `preg`"
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
            name="🎭 Personality",
            value=(
                "`?kat mood` `roast @user` `compliment @user`\n"
                "`?kat judge @user` `wisdom` `chaos`"
            ),
            inline=False,
        )

        embed.add_field(
            name="🎮 Games",
            value=(
                "`?kat coinflip` `8ball <question>`\n"
                "`?kat roll [count] [sides]`"
            ),
            inline=False,
        )

        embed.add_field(
            name="🤖 AI & OCR",
            value=(
                "**AI:** Mention Kat + your message to chat with AI.\n"
                "**OCR:** Attach an image + `?kat ocr`"
            ),
            inline=False,
        )

        embed.add_field(
            name="🎞️ GIFs",
            value="`?kat gifs` `?kat gifs <action>`",
            inline=False,
        )

        embed.add_field(
            name="🛠️ GIF Management",
            value=(
                "`?kat addgif <action>`\n"
                "`?kat removegif <action> <number>`"
            ),
            inline=False,
        )

        embed.add_field(
            name="👀 Automatic",
            value="Kat may randomly react to certain words or phrases.",
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