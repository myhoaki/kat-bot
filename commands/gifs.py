import os
import re

import discord
from discord.ext import commands


GIF_FOLDER = "/app/gifs"
MAX_FILE_SIZE = 8 * 1024 * 1024

ALLOWED_ACTIONS = (
    "hug",
    "kiss",
    "pat",
    "slap",
    "cuddle",
    "highfive",
    "preg",
)

MANAGER_ROLE = "Kat Manager"


def get_next_gif_number(folder):
    """
    Find the lowest available GIF number.

    Example:
        hug001.gif
        hug002.gif
        hug004.gif

    The next upload becomes:
        hug003.gif
    """

    os.makedirs(folder, exist_ok=True)

    numbers = []

    pattern = re.compile(
        r"^.*?(\d+)\.gif$",
        re.IGNORECASE,
    )

    for filename in os.listdir(folder):
        match = pattern.match(filename)

        if match:
            numbers.append(
                int(match.group(1))
            )

    number = 1

    while number in numbers:
        number += 1

    return number


def has_manager_role(member: discord.Member) -> bool:
    """
    Check whether the user has the Kat Manager role.
    """

    return any(
        role.name == MANAGER_ROLE
        for role in member.roles
    )


class GifCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gifs")
    async def gifs(
        self,
        ctx,
        action: str = None,
    ):
        """
        List available GIFs.

        ?kat gifs
        ?kat gifs hug
        """

        if action:
            action = action.lower()

            if action not in ALLOWED_ACTIONS:
                await ctx.send(
                    f"Unknown action: **{action}**\n"
                    f"Available actions: "
                    f"{', '.join(ALLOWED_ACTIONS)}"
                )
                return

            folder = os.path.join(
                GIF_FOLDER,
                action,
            )

            if not os.path.exists(folder):
                await ctx.send(
                    f"No GIF folder exists for "
                    f"**{action}** yet."
                )
                return

            gifs = sorted(
                filename
                for filename in os.listdir(folder)
                if filename.lower().endswith(".gif")
            )

            if not gifs:
                await ctx.send(
                    f"No GIFs found for **{action}**."
                )
                return

            lines = []

            for index, filename in enumerate(
                gifs,
                start=1,
            ):
                lines.append(
                    f"**{index}.** `{filename}`"
                )

            await ctx.send(
                f"🎬 **{action.upper()} GIFs**\n"
                + "\n".join(lines)
            )
            return

        lines = []

        for action_name in ALLOWED_ACTIONS:
            folder = os.path.join(
                GIF_FOLDER,
                action_name,
            )

            if not os.path.exists(folder):
                count = 0
            else:
                count = sum(
                    1
                    for filename in os.listdir(folder)
                    if filename.lower().endswith(".gif")
                )

            lines.append(
                f"**{action_name}** — {count} GIF(s)"
            )

        await ctx.send(
            "🎬 **Kat's GIF Library**\n"
            + "\n".join(lines)
        )

    @commands.command(name="addgif")
    async def addgif(
        self,
        ctx,
        action: str,
    ):
        """
        Upload a GIF to an action.

        Requires the Kat Manager role.
        """

        if not isinstance(
            ctx.author,
            discord.Member,
        ):
            return

        if not has_manager_role(ctx.author):
            await ctx.send(
                f"{ctx.author.mention} "
                "you need the **Kat Manager** role "
                "to add GIFs. 🐱"
            )
            return

        action = action.lower()

        if action not in ALLOWED_ACTIONS:
            await ctx.send(
                f"Unknown action: **{action}**\n"
                f"Available actions: "
                f"{', '.join(ALLOWED_ACTIONS)}"
            )
            return

        if not ctx.message.attachments:
            await ctx.send(
                "Attach a `.gif` file to the command. 😭"
            )
            return

        attachment = ctx.message.attachments[0]

        if not attachment.filename.lower().endswith(
            ".gif"
        ):
            await ctx.send(
                "That isn't a GIF. "
                "Kat refuses to accept your suspicious file. 💀"
            )
            return

        if attachment.size > MAX_FILE_SIZE:
            await ctx.send(
                "That GIF is too fucking large. 💀\n"
                "Maximum size is **8 MB**."
            )
            return

        folder = os.path.join(
            GIF_FOLDER,
            action,
        )

        os.makedirs(
            folder,
            exist_ok=True,
        )

        number = get_next_gif_number(
            folder
        )

        filename = (
            f"{action}{number:03d}.gif"
        )

        filepath = os.path.join(
            folder,
            filename,
        )

        try:
            await attachment.save(filepath)

        except (discord.HTTPException, OSError) as exc:
            await ctx.send(
                "Kat couldn't save that GIF. 😭\n"
                f"`{exc}`"
            )
            return

        await ctx.send(
            f"✅ Added `{filename}` to "
            f"**{action}**."
        )

    @commands.command(name="removegif")
    async def removegif(
        self,
        ctx,
        action: str,
        number: int,
    ):
        """
        Remove a GIF by its displayed list number.

        Requires the Kat Manager role.
        """

        if not isinstance(
            ctx.author,
            discord.Member,
        ):
            return

        if not has_manager_role(ctx.author):
            await ctx.send(
                f"{ctx.author.mention} "
                "you need the **Kat Manager** role "
                "to remove GIFs. 🐱"
            )
            return

        action = action.lower()

        if action not in ALLOWED_ACTIONS:
            await ctx.send(
                f"Unknown action: **{action}**\n"
                f"Available actions: "
                f"{', '.join(ALLOWED_ACTIONS)}"
            )
            return

        folder = os.path.join(
            GIF_FOLDER,
            action,
        )

        if not os.path.exists(folder):
            await ctx.send(
                f"No GIF folder exists for "
                f"**{action}**."
            )
            return

        gifs = sorted(
            filename
            for filename in os.listdir(folder)
            if filename.lower().endswith(".gif")
        )

        if not gifs:
            await ctx.send(
                f"No GIFs found for **{action}**."
            )
            return

        if number < 1 or number > len(gifs):
            await ctx.send(
                f"Invalid GIF number. "
                f"Choose between **1** and **{len(gifs)}**."
            )
            return

        filename = gifs[number - 1]
        filepath = os.path.join(
            folder,
            filename,
        )

        try:
            os.remove(filepath)

        except OSError as exc:
            await ctx.send(
                "Kat couldn't remove that GIF. 😭\n"
                f"`{exc}`"
            )
            return

        await ctx.send(
            f"🗑️ Removed `{filename}` from "
            f"**{action}**."
        )


async def setup(bot):
    await bot.add_cog(
        GifCommands(bot)
    )