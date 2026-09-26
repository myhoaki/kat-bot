import discord
from discord.ext import commands

from core.relationships import (
    generate_relationship,
    relationship_verdict,
)


class RelationshipCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ship")
    async def ship(
        self,
        ctx,
        user1: discord.Member,
        user2: discord.Member,
    ):
        stats = generate_relationship(
            user1.id,
            user2.id,
        )

        verdict = relationship_verdict(stats)

        embed = self.make_relationship_embed(
            user1,
            user2,
            stats,
            verdict,
            "💕 Relationship Analysis",
        )

        await ctx.send(embed=embed)

    @commands.command(name="relationship")
    async def relationship(
        self,
        ctx,
        user1: discord.Member,
        user2: discord.Member,
    ):
        stats = generate_relationship(
            user1.id,
            user2.id,
        )

        verdict = relationship_verdict(stats)

        embed = self.make_relationship_embed(
            user1,
            user2,
            stats,
            verdict,
            "🐱 Kat's Relationship Report",
        )

        await ctx.send(embed=embed)

    @commands.command(name="friendship")
    async def friendship(
        self,
        ctx,
        member: discord.Member,
    ):
        stats = generate_relationship(
            ctx.author.id,
            member.id,
        )

        friendship = stats["friendship"]

        if friendship >= 90:
            verdict = "Besties. Absolutely inseparable. 🫂"
        elif friendship >= 75:
            verdict = "Certified bestie material. 🥰"
        elif friendship >= 60:
            verdict = "Pretty solid friendship! 🤝"
        elif friendship >= 40:
            verdict = "You two are getting there."
        elif friendship >= 20:
            verdict = "Acquaintances at best. 💀"
        else:
            verdict = (
                "Kat suggests introducing "
                "yourselves first. 😭"
            )

        embed = discord.Embed(
            title="🤝 Friendship Check",
            description=(
                f"**{ctx.author.display_name} × "
                f"{member.display_name}**"
            ),
        )

        embed.add_field(
            name="Friendship",
            value=f"**{friendship}%**",
            inline=False,
        )

        embed.add_field(
            name="Kat's Opinion",
            value=verdict,
            inline=False,
        )

        await ctx.send(embed=embed)

    @staticmethod
    def make_relationship_embed(
        user1,
        user2,
        stats,
        verdict,
        title,
    ):
        embed = discord.Embed(
            title=title,
            description=(
                f"**{user1.display_name} × "
                f"{user2.display_name}**"
            ),
        )

        embed.add_field(
            name="❤️ Romance",
            value=f"**{stats['romance']}%**",
            inline=True,
        )

        embed.add_field(
            name="🤝 Friendship",
            value=f"**{stats['friendship']}%**",
            inline=True,
        )

        embed.add_field(
            name="🔥 Chemistry",
            value=f"**{stats['chemistry']}%**",
            inline=True,
        )

        embed.add_field(
            name="💀 Chaos Compatibility",
            value=f"**{stats['chaos']}%**",
            inline=True,
        )

        embed.add_field(
            name="🐱 Kat's Approval",
            value=f"**{stats['kat_approval']}%**",
            inline=True,
        )

        embed.add_field(
            name="🔮 Kat's Verdict",
            value=f"**{verdict}**",
            inline=False,
        )

        return embed


async def setup(bot):
    await bot.add_cog(
        RelationshipCommands(bot)
    )