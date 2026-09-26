import os
import random

import discord
from discord.ext import commands


async def send_action(
    ctx: commands.Context,
    member: discord.Member,
    action: str,
    message: str,
):
    gif_folder = f"/app/gifs/{action}"

    if not os.path.exists(gif_folder):
        await ctx.send(
            f"{ctx.author.mention} {message} "
            "but this action doesn't have a GIF folder yet 😭"
        )
        return

    gifs = [
        filename
        for filename in os.listdir(gif_folder)
        if filename.lower().endswith(".gif")
    ]

    if not gifs:
        await ctx.send(
            f"{ctx.author.mention} {message} "
            "but I couldn't find any GIFs 😭"
        )
        return

    gif = random.choice(gifs)
    gif_path = os.path.join(gif_folder, gif)

    await ctx.send(
        content=f"{ctx.author.mention} {message}",
        file=discord.File(
            gif_path,
            filename=gif,
        ),
    )
