import os
import re

from discord.ext import commands


GIF_ROOT = "/app/gifs"

ALLOWED_ACTIONS = {
    "hug",
    "kiss",
    "pat",
    "slap",
    "cuddle",
    "highfive",
    "preg",
}

MAX_FILE_SIZE = 8 * 1024 * 1024  # 8 MB
MAX_DISPLAYED_GIFS = 50


def get_next_filename(folder: str, action: str) -> str:
    pattern = re.compile(
        rf"^{re.escape(action)}(\d+)\.gif$",
        re.IGNORECASE,
    )

    used_numbers = set()

    if os.path.isdir(folder):
        for filename in os.listdir(folder):
            match = pattern.match(filename)

            if match:
                used_numbers.add(
                    int(match.group(1))
                )

    number = 1

    while number in used_numbers:
        number += 1

    return f"{action}{number:03d}.gif"


def get_gif_files(folder: str) -> list[str]:
    if not os.path.isdir(folder):
        return []

    return sorted(
        filename
        for filename in os.listdir(folder)
        if filename.lower().endswith(".gif")
    )


class GifCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gifs")
    async def gifs(
        self,
        ctx,
        action: str | None = None,
    ):
        # ?kat gifs
        if action is None:
            lines = [
                "🐱 **Available GIF actions:**",
                "",
            ]

            for name in sorted(ALLOWED_ACTIONS):
                folder = os.path.join(
                    GIF_ROOT,
                    name,
                )

                gif_count = len(
                    get_gif_files(folder)
                )

                lines.append(
                    f"• **{name}** — {gif_count} GIF(s)"
                )

            lines.extend(
                (
                    "",
                    "Use `?kat gifs <action>` "
                    "to see the GIFs.",
                    "Example: `?kat gifs hug`",
                )
            )

            await ctx.send(
                "\n".join(lines)
            )
            return

        action = action.lower()

        if action not in ALLOWED_ACTIONS:
            await ctx.send(
                "❌ Unknown GIF action.\n"
                "Use `?kat gifs` to see the available actions."
            )
            return

        folder = os.path.join(
            GIF_ROOT,
            action,
        )

        gifs = get_gif_files(folder)

        if not gifs:
            await ctx.send(
                f"🐱 There are currently no GIFs "
                f"for `{action}`."
            )
            return

        displayed = gifs[
            :MAX_DISPLAYED_GIFS
        ]

        lines = [
            f"🐱 **{action.title()} GIFs ({len(gifs)})**",
            "",
        ]

        for index, filename in enumerate(
            displayed,
            start=1,
        ):
            lines.append(
                f"`{index}.` {filename}"
            )

        if len(gifs) > MAX_DISPLAYED_GIFS:
            lines.extend(
                (
                    "",
                    f"...and {len(gifs) - MAX_DISPLAYED_GIFS} more.",
                )
            )

        await ctx.send(
            "\n".join(lines)
        )

    @commands.command(name="addgif")
    @commands.has_guild_permissions(
        manage_guild=True
    )
    async def addgif(
        self,
        ctx,
        action: str,
    ):
        action = action.lower()

        if action not in ALLOWED_ACTIONS:
            await ctx.send(
                "❌ Unknown GIF action.\n"
                "Use `?kat gifs` to see the available actions."
            )
            return

        if not ctx.message.attachments:
            await ctx.send(
                "📎 Attach a `.gif` to your message.\n"
                f"Example: `?kat addgif {action}`"
            )
            return

        attachment = ctx.message.attachments[0]
        filename = attachment.filename.lower()

        if not filename.endswith(".gif"):
            await ctx.send(
                "❌ I only accept `.gif` files."
            )
            return

        if attachment.size > MAX_FILE_SIZE:
            await ctx.send(
                "❌ That GIF is too large.\n"
                "The maximum size is **8 MB**."
            )
            return

        folder = os.path.join(
            GIF_ROOT,
            action,
        )

        os.makedirs(
            folder,
            exist_ok=True,
        )

        new_filename = get_next_filename(
            folder,
            action,
        )

        destination = os.path.join(
            folder,
            new_filename,
        )

        try:
            # Save the GIF exactly as uploaded.
            await attachment.save(
                destination
            )

        except Exception as exc:
            print(
                f"Failed to save GIF: {exc}",
                flush=True,
            )

            await ctx.send(
                "❌ I couldn't save that GIF."
            )
            return

        await ctx.send(
            f"🐱 **GIF added!**\n"
            f"Action: `{action}`\n"
            f"File: `{new_filename}`"
        )

    @commands.command(name="removegif")
    @commands.has_guild_permissions(
        manage_guild=True
    )
    async def removegif(
        self,
        ctx,
        action: str,
        gif_number: int,
    ):
        action = action.lower()

        if action not in ALLOWED_ACTIONS:
            await ctx.send(
                "❌ Unknown GIF action.\n"
                "Use `?kat gifs` to see the available actions."
            )
            return

        if gif_number < 1:
            await ctx.send(
                "❌ GIF number must be **1 or higher**."
            )
            return

        folder = os.path.join(
            GIF_ROOT,
            action,
        )

        gifs = get_gif_files(folder)

        if not gifs:
            await ctx.send(
                f"🐱 There are no GIFs for `{action}`."
            )
            return

        if gif_number > len(gifs):
            await ctx.send(
                f"❌ GIF number `{gif_number}` "
                f"doesn't exist.\n"
                f"There are only **{len(gifs)}** GIF(s) "
                f"for `{action}`."
            )
            return

        filename = gifs[
            gif_number - 1
        ]

        file_path = os.path.join(
            folder,
            filename,
        )

        try:
            os.remove(file_path)

        except FileNotFoundError:
            await ctx.send(
                "❌ That GIF no longer exists."
            )
            return

        except OSError as exc:
            print(
                f"Failed to remove GIF: {exc}",
                flush=True,
            )

            await ctx.send(
                "❌ I couldn't remove that GIF."
            )
            return

        await ctx.send(
            f"🗑️ **GIF removed!**\n"
            f"Action: `{action}`\n"
            f"File: `{filename}`"
        )

    @addgif.error
    async def addgif_error(
        self,
        ctx,
        error,
    ):
        if isinstance(
            error,
            commands.MissingPermissions,
        ):
            await ctx.send(
                "🔒 You need **Manage Server** "
                "permission to add GIFs."
            )
            return

        if isinstance(
            error,
            commands.MissingRequiredArgument,
        ):
            await ctx.send(
                "📁 Tell me which action to add "
                "the GIF to.\n"
                "Example: `?kat addgif hug`"
            )
            return

        raise error

    @removegif.error
    async def removegif_error(
        self,
        ctx,
        error,
    ):
        if isinstance(
            error,
            commands.MissingPermissions,
        ):
            await ctx.send(
                "🔒 You need **Manage Server** "
                "permission to remove GIFs."
            )
            return

        if isinstance(
            error,
            commands.MissingRequiredArgument,
        ):
            await ctx.send(
                "🗑️ Tell me the action and GIF number.\n"
                "Example: `?kat removegif hug 3`"
            )
            return

        if isinstance(
            error,
            commands.BadArgument,
        ):
            await ctx.send(
                "❌ GIF number must be a number.\n"
                "Example: `?kat removegif hug 3`"
            )
            return

        raise error


async def setup(bot):
    await bot.add_cog(
        GifCommands(bot)
    )