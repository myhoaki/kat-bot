import random

import discord
from discord.ext import commands

from core.relationships import (
    apply_action_relationship,
    generate_relationship,
    get_relationship_cooldown_remaining,
    kat_relationship_reaction,
    relationship_verdict,
    start_relationship_cooldown,
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

        romance = stats["romance"]
        chemistry = stats["chemistry"]

        ship_score = round(
            (romance + chemistry) / 2
        )

        if ship_score >= 90:
            verdict = (
                "GET A FUCKING ROOM. 💀"
            )
        elif ship_score >= 80:
            verdict = (
                "Kat is VERY suspicious of you two. 👀"
            )
        elif ship_score >= 70:
            verdict = (
                "Okay... there is definitely "
                "something going on here. 😳"
            )
        elif ship_score >= 55:
            verdict = (
                "Hmm. There's potential. "
                "Don't fuck it up."
            )
        elif ship_score >= 40:
            verdict = (
                "Maybe. Kat isn't convinced yet. 🤨"
            )
        elif ship_score >= 20:
            verdict = (
                "This ship is taking on water. 🚢💀"
            )
        else:
            verdict = (
                "Kat has officially sunk the ship. 🚢💀"
            )

        embed = discord.Embed(
            title="💕 Ship Check",
            description=(
                f"**{user1.display_name} × "
                f"{user2.display_name}**"
            ),
        )

        embed.add_field(
            name="💕 Romance",
            value=f"**{romance}%**",
            inline=True,
        )

        embed.add_field(
            name="🔥 Chemistry",
            value=f"**{chemistry}%**",
            inline=True,
        )

        embed.add_field(
            name="💘 Ship Score",
            value=f"**{ship_score}%**",
            inline=False,
        )

        embed.add_field(
            name="🐱 Kat's Verdict",
            value=verdict,
            inline=False,
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
            verdict = (
                "Besties. Absolutely inseparable. 🫂"
            )
        elif friendship >= 75:
            verdict = (
                "Certified bestie material. 🥰"
            )
        elif friendship >= 60:
            verdict = (
                "Pretty solid friendship! 🤝"
            )
        elif friendship >= 40:
            verdict = (
                "You two are getting there."
            )
        elif friendship >= 20:
            verdict = (
                "Acquaintances at best. 💀"
            )
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

    @commands.command(name="relationtest")
    async def relationtest(
        self,
        ctx,
        member: discord.Member,
    ):
        remaining = get_relationship_cooldown_remaining(
            ctx.author.id
        )

        if remaining > 0:
            await ctx.send(
                f"{ctx.author.mention} calm the fuck down. 💀\n"
                f"You need to wait **{remaining:.0f}s** "
                f"before testing another relationship event."
            )
            return

        start_relationship_cooldown(
            ctx.author.id
        )

        actions = (
            "hug",
            "kiss",
            "pat",
            "cuddle",
            "highfive",
            "slap",
            "preg",
        )

        action = random.choice(actions)

        stats, changes = apply_action_relationship(
            ctx.author.id,
            member.id,
            action,
        )

        change_text = self.format_changes(
            changes
        )

        reaction = kat_relationship_reaction(
            stats
        )

        embed = discord.Embed(
            title="🎲 Relationship RNG Test",
            description=(
                f"**{ctx.author.display_name} × "
                f"{member.display_name}**"
            ),
        )

        embed.add_field(
            name="Event",
            value=f"**{action}**",
            inline=False,
        )

        embed.add_field(
            name="Relationship Changes",
            value=change_text,
            inline=False,
        )

        embed.add_field(
            name="Kat's Reaction",
            value=reaction,
            inline=False,
        )

        await ctx.send(embed=embed)

@staticmethod
def format_changes(changes):
    emojis = {
        "romance": "💕",
        "friendship": "🤝",
        "chemistry": "🔥",
        "chaos": "💀",
        "kat_approval": "🐱",
    }

    parts = []

    for stat, change in changes.items():
        if change == 0:
            continue

        if change > 0:
            amount = f"+{change}"
        else:
            amount = f"−{abs(change)}"

        parts.append(
            f"{emojis.get(stat, '📊')} **{amount}**"
        )

    if not parts:
        return "No change."

    return "  ".join(parts)


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

        embed.add_field(
            name="🐱 Kat's Opinion",
            value=kat_relationship_reaction(
                stats
            ),
            inline=False,
        )

        return embed


async def setup(bot):
    await bot.add_cog(
        RelationshipCommands(bot)
    )