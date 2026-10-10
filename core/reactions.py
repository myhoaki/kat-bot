import random
import re
import time

CHANNEL_COOLDOWN = 90
USER_COOLDOWN = 180
REACTION_CHANCE = 0.08

last_channel_reaction = {}
last_user_reaction = {}

EMOTES = {
    r"\b(sus|suspicious|theor(y|ise|ize)|explain|how does that work)\b":
        "<:MonkaThink:1337409772177330197>",
    r"\b(awkward|cringe|embarrassing|yikes|painful|secondhand embarrassment)\b":
        "<:worryOld:1491473285014097930>",
    r"\b(wtf|what the hell|no way|insane|unbelievable\b":
        "<:MonkaGiga:945541709159337984>",
    r"\b(yikes|oh no|concerned|worry|uncomfortable|disaster)\b":
        "<:WorrySweat:956031327348617266>",
}


async def maybe_react(message, own_bot_id, partner_bot_id):
    if message.author.id == own_bot_id:
        return

    if message.author.bot and message.author.id != partner_bot_id:
        return

    content = message.content.strip().lower()
    if not content or content.startswith("?"):
        return

    candidates = [
        emote for pattern, emote in EMOTES.items()
        if re.search(pattern, content, re.IGNORECASE)
    ]
    if not candidates or random.random() > REACTION_CHANCE:
        return

    now = time.monotonic()
    channel_id = message.channel.id
    user_id = message.author.id

    if now - last_channel_reaction.get(channel_id, 0) < CHANNEL_COOLDOWN:
        return
    if now - last_user_reaction.get(user_id, 0) < USER_COOLDOWN:
        return

    try:
        await message.add_reaction(random.choice(candidates))
    except Exception as exc:
        print(f"[Reactions] Failed to react: {exc}", flush=True)
        return

    last_channel_reaction[channel_id] = time.monotonic()
    last_user_reaction[user_id] = time.monotonic()
