import os
import random

import discord
from discord.ext import commands

from core.personality import random_reaction
from core.relationships import (
    apply_action_relationship,
    get_relationship_cooldown_remaining,
    start_relationship_cooldown,
)


async def send_action(
    ctx: commands.Context,
    member: discord.Member,
    action: str,
    message: str,
):
    # Check relationship RNG cooldown.
    remaining = get_relationship_cooldown_remaining(
        ctx.author.id
    )

    if remaining > 0:
        await ctx.send(
            f"{ctx.author.mention} calm the fuck down. 💀\n"
            f"You need to wait **{remaining:.0f}s** "
            f"before using another relationship action."
        )
        return

    # Start cooldown.
    start_relationship_cooldown(
        ctx.author.id
    )

    # Apply relationship RNG.
    stats, changes = apply_action_relationship(
        ctx.author.id,
        member.id,
        action,
    )

    relationship_text = format_relationship_changes(
        changes
    )

    gif_folder = f"/app/gifs/{action}"

    if not os.path.exists(gif_folder):
        await ctx.send(
            f"{ctx.author.mention} {message}\n"
            f"{random_reaction(action)}\n"
            f"{relationship_text}\n"
            "But this action doesn't have a GIF folder yet 😭"
        )
        return

    gifs = [
        filename
        for filename in os.listdir(gif_folder)
        if filename.lower().endswith(".gif")
    ]

    if not gifs:
        await ctx.send(
            f"{ctx.author.mention} {message}\n"
            f"{random_reaction(action)}\n"
            f"{relationship_text}\n"
            "But I couldn't find any GIFs 😭"
        )
        return

    gif = random.choice(gifs)
    gif_path = os.path.join(
        gif_folder,
        gif,
    )

    await ctx.send(
        content=(
            f"{ctx.author.mention} {message}\n"
            f"{random_reaction(action)}\n"
            f"{relationship_text}"
        ),
        file=discord.File(
            gif_path,
            filename=gif,
        ),
    )

def format_relationship_changes(changes):
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
        return "💞 **Relationship Shift:** No change"

    return (
        "💞 **Relationship Shift:** "
        + "  ".join(parts)
    )

