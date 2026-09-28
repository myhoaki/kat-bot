import random
import time


REACTION_CHANCE = 0.2
COOLDOWN_SECONDS = 60

last_reaction = 0.0


REACTIONS = {
    "magical_girl": {
        "emoji": [
            "💅",
        ],
        "messages": [
            "Oh brilliant. More sparkles. Just what this fucking server needed.",
            "Jesus Christ, it's a magical girl. We're fucked.",
            "Right. Because apparently regular anime wasn't degenerate enough.",
            "Look at this shit. Transformation sequence and everything.",
            "Someone's discovered magical girls and immediately lost the plot.",
            "Well, that's one way to spend your evening. Bloody hell.",
            "Kat's seen enough. And yet somehow she's still looking.",
            "Absolutely fucking shameless. I respect the commitment.",
        ],
    },

    "maid": {
        "emoji": [
            "🧹",
        ],
        "messages": [
            "Oh for fuck's sake. Someone mentioned maids.",
            "A maid outfit? Of course. You lot never disappoint.",
            "Right, because apparently housekeeping is attractive now.",
            "Look at you lot. One maid outfit and everyone's fucking useless.",
            "Someone needs to confiscate the internet from this server.",
            "A maid, eh? Suddenly everyone's got excellent manners.",
            "Christ. You people are predictable as fucking gravity.",
            "Kat isn't judging. She's absolutely judging.",
        ],
    },

    "ntr": {
        "emoji": [
            "💀",
        ],
        "messages": [
            "Oh, fuck off. We're not doing this today.",
            "Right. That's enough internet for one fucking day.",
            "What the actual fuck did I just read?",
            "Brilliant. Someone's brought the cursed shit into chat.",
            "Nope. Kat's not getting involved in whatever the fuck this is.",
            "We've crossed a line somewhere. I'm just not sure which one.",
            "Who the fuck thought this was a good idea?",
            "Kat would like to formally deny witnessing this conversation.",
        ],
    },

    "bunny_suit": {
        "emoji": [
            "👯‍♀️",
        ],
        "messages": [
            "A bunny suit. Naturally. What else would you degenerates come up with?",
            "Well, there goes the last shred of dignity in this server.",
            "Someone saw a bunny suit and immediately forgot how to behave.",
            "Christ alive. You lot are fucking predictable.",
            "Bunny suit detected. Brain cells immediately evacuated.",
            "Oh good. We've reached the bunny suit stage of the degeneracy.",
            "Kat has questions. None of them are appropriate for public discussion.",
            "Right. Keep staring at the fictional woman. I'm sure that'll end well.",
        ],
    },

    "australia": {
        "emoji": [
            "🦘",
        ],
        "messages": [
            "Australia, eh? Fucking hell. Here we go.",
            "An Aussie. Right. Hide the beer and lock up the kangaroos.",
            "G'day, you bloody menace. 🇦🇺",
            "Australia mentioned. Somewhere, a kangaroo just threw a punch.",
            "Ah yes, Australia. Where even the wildlife has an anger problem.",
            "Aussie detected. Try not to start a fight before lunch.",
            "Oz, mate. Absolutely fucking feral.",
            "Right, who's brought the Australian into the chat?",
        ],
    },
}


def can_react() -> bool:
    global last_reaction

    now = time.monotonic()

    if now - last_reaction < COOLDOWN_SECONDS:
        return False

    if random.random() > REACTION_CHANCE:
        return False

    last_reaction = now
    return True


def get_reaction(message_content: str):
    text = message_content.lower()

    if any(
        word in text
        for word in (
            "magical girl",
            "magic girl",
            "madoka",
        )
    ):
        category = "magical_girl"

    elif any(
        word in text
        for word in (
            "bunny suit",
            "bunny girl",
        )
    ):
        category = "bunny_suit"

    elif any(
        word in text
        for word in (
            "ntr",
            "netorare",
        )
    ):
        category = "ntr"

    elif any(
        word in text
        for word in (
            "maido",
            "maid",
        )
    ):
        category = "maid"

    elif any(
        word in text
        for word in (
            "australia",
            "aussie",
            "oz",
            "aus",
        )
    ):
        category = "australia"

    else:
        return None

    if not can_react():
        return None

    return {
        "message": random.choice(
            REACTIONS[category]["messages"]
        ),
        "emoji": random.choice(
            REACTIONS[category]["emoji"]
        ),
    }