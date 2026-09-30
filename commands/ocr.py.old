import io

import aiohttp
import discord
from discord.ext import commands

OCR_URL = "http://manga-ocr:8000"


class OCR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ocr")
    async def ocr(self, ctx):
        """OCR a manga image attached to the message."""

        if not ctx.message.attachments:
            await ctx.send("🐱 Attach a manga image to the message.")
            return

        attachment = ctx.message.attachments[0]

        if not attachment.content_type or not attachment.content_type.startswith("image/"):
            await ctx.send("🐱 That doesn't look like an image.")
            return

        async with ctx.typing():
            try:
                image_data = await attachment.read()

                form = aiohttp.FormData()
                form.add_field(
                    "image",
                    image_data,
                    filename=attachment.filename,
                    content_type=attachment.content_type,
                )

                timeout = aiohttp.ClientTimeout(total=60)

                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.post(
                        f"{OCR_URL}/manga-ocr",
                        data=form,
                    ) as response:

                        if response.status != 200:
                            error = await response.text()
                            await ctx.send(
                                f"🐱 OCR server returned `{response.status}`.\n"
                                f"```{error[:1000]}```"
                            )
                            return

                        result = await response.json()

                text = str(result).strip()

                if not text or text == "None":
                    await ctx.send("🐱 I couldn't find any text in that image.")
                    return

                if len(text) > 1900:
                    text = text[:1900] + "\n..."

                await ctx.send(
                    f"🇯🇵 **OCR result:**\n"
                    f"```text\n{text}\n```"
                )

            except aiohttp.ClientError as e:
                print(f"OCR connection error: {e}", flush=True)
                await ctx.send("🐱 I can't reach the manga OCR server.")

            except Exception as e:
                print(f"OCR error: {e}", flush=True)
                await ctx.send("🐱 Something went wrong while processing the image.")


async def setup(bot):
    await bot.add_cog(OCR(bot))