import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Kat Bot Commands",
            color=discord.Color.blurple(),
        )

        embed.add_field(
            name="Interactions",
            value=(
                "`?kat hug @member` `kiss` `pat` `slap`\n"
                "`cuddle` `highfive` `preg`"
            ),
            inline=False,
        )

        embed.add_field(
            name="Games",
            value=(
                "`?kat coinflip` `8ball <question>`\n"
                "`?kat roll [count] [sides]`"
            ),
            inline=False,
        )

        embed.add_field(
            name="AI",
            value=(
                "`Mention Kat Bot + your message`\n"
                "`?kat personality`\n"
                "`?kat personality <name>`"
            ),
            inline=False,
        )

        embed.add_field(
            name="TTS",
            value=(
                "`?kat say <text>`\n"
                "`?kat say <text> -jp`"
            ),
            inline=False,
        )
        
        embed.add_field(
        name="GIFs",
        value=(
            "`?kat gifs` `?kat gifs <action>`\n"
            "`?kat addgif <action>`\n"
            "`?kat removegif <action> <number>`"
        ),
        inline=False,
        )

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(HelpCommands(bot))
