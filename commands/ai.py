import asyncio
import random
import re
import time

import discord
from discord.ext import commands

from core.ai import (
    can_use_ai,
    get_ai_reply,
    mark_ai_used,
)


class AI(commands.Cog):
    ANI_BOT_ID = 1557222231166160976
    CONVERSATION_TIMEOUT = 120
    ANI_BURST_WAIT = (2.8, 3.6)

    def __init__(self, bot):
        self.bot = bot
        self.ani_conversations = {}
        self.ani_pending = {}
        self.ani_bursts = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        is_ani = (
            message.author.bot
            and message.author.id == self.ANI_BOT_ID
        )

        if message.author.bot and not is_ani:
            return

        if message.content.startswith("?kat"):
            return

        now = time.monotonic()
        key = (message.channel.id, self.ANI_BOT_ID)
        last_ani_message = self.ani_conversations.get(key, 0)
        ani_conversation_active = (
            is_ani
            and now - last_ani_message < self.CONVERSATION_TIMEOUT
        )

        kat_was_mentioned = (
            self.bot.user is not None
            and any(user.id == self.bot.user.id for user in message.mentions)
        )

        # Collect Ani's consecutive messages and answer the whole thought.
        if is_ani:
            if not kat_was_mentioned and not ani_conversation_active:
                print(
                    "[AI] Ignoring Ani: no Kat mention and no active conversation.",
                    flush=True,
                )
                return

            self.ani_conversations[key] = now
            self.ani_bursts.setdefault(key, []).append(message.content)

            pending = self.ani_pending.get(key)
            if pending and not pending.done():
                pending.cancel()

            self.ani_pending[key] = asyncio.create_task(
                self._reply_after_ani_burst(
                    message.channel,
                    key,
                    message.author.display_name,
                )
            )
            return

        # Human users must mention Kat to trigger a reply.
        if not kat_was_mentioned:
            return

        if not can_use_ai(message.author.id):
            await message.reply(
                "Give me a fucking second. 💀",
                mention_author=False,
            )
            return

        user_message = re.sub(
            rf"<@!?{self.bot.user.id}>",
            "",
            message.content,
        ).strip()

        if not user_message:
            user_message = "Someone just mentioned me. Say something funny."

        await self._generate_and_send(
            message.channel,
            user_message,
            message.author.display_name,
            message.author.id,
            human=True,
        )

    async def _reply_after_ani_burst(self, channel, key, display_name):
        try:
            await asyncio.sleep(random.uniform(*self.ANI_BURST_WAIT))

            messages = self.ani_bursts.pop(key, [])
            self.ani_pending.pop(key, None)

            if not messages:
                return

            combined = "\n".join(messages)
            combined = re.sub(
                rf"<@!?{self.bot.user.id}>",
                "",
                combined,
            ).strip()

            if not combined:
                combined = "Ani mentioned me. Say something funny."

            await self._generate_and_send(
                channel,
                combined,
                display_name,
                self.ANI_BOT_ID,
                human=False,
            )
        except asyncio.CancelledError:
            # A newer Ani message arrived; wait for the new burst to finish.
            raise
        except Exception as exc:
            print(f"[AI] Error handling Ani's message burst: {exc}", flush=True)

    async def _generate_and_send(
        self,
        channel,
        user_message,
        display_name,
        author_id,
        *,
        human,
    ):
        try:
            async with channel.typing():
                reply = await self.bot.loop.run_in_executor(
                    None,
                    get_ai_reply,
                    user_message,
                    channel.id,
                    display_name,
                )

            if not reply:
                if human:
                    await channel.send(
                        "Kat's brain just blue-screened. Try again in a few seconds."
                    )
                return

            # Small, variable pause before Kat speaks.
            await asyncio.sleep(random.uniform(1.2, 2.6))
            await channel.send(reply)

            if human:
                mark_ai_used(author_id)

        except asyncio.CancelledError:
            raise
        except discord.HTTPException as exc:
            print(f"[AI] Failed to send AI reply: {exc}", flush=True)
        except Exception as exc:
            print(f"[AI] Unexpected Discord AI error: {exc}", flush=True)


async def setup(bot):
    await bot.add_cog(AI(bot))
