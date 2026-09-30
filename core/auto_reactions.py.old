import random
import time
import re

REACTION_CHANCE = 0.2
COOLDOWN_SECONDS = 60

last_reaction = 0.0


REACTIONS = {
    "magical_girl": {
        "emoji": [
            "💅",
        ],
        "messages": [
            "Oh brilliant. Magical girls. Because apparently one anime wasn't enough sparkles for this fucking server.",
            "Jesus Christ, it's a magical girl. Someone hide the transformation sequence budget.",
            "Right. More sparkles, friendship speeches, and suspiciously powerful teenagers. Classic.",
            "Ah yes, the sacred anime ritual: scream, transform, defeat god. Very normal behavior.",
            "Someone discovered magical girls and immediately unlocked their inner weeb. Tragic.",
            "Magical girl detected. Somebody's about to yell the name of an attack for 45 seconds.",
            "Power of friendship? In this economy? Fucking delusional.",
            "Kat has seen this arc before. It ends with trauma, merch, and 47 episodes of filler.",
        ],
    },

    "maid": {
        "emoji": [
            "🧹",
        ],
        "messages": [
            "Oh for fuck's sake. Someone mentioned maids and the weebs have assembled.",
            "A maid outfit? Naturally. Suddenly every anime protagonist has lost the ability to behave normally.",
            "Right. Because apparently cleaning the house becomes a character archetype if you add enough anime.",
            "One maid appears and suddenly everyone's pretending they're the protagonist. Pathetic.",
            "Ah yes, the classic anime maid. Efficient, adorable, and somehow more dangerous than the main villain.",
            "Maid detected. Somewhere, a seasonal anime just gained another 10,000 viewers.",
            "Christ. You people hear 'maid' and immediately start speaking in anime dialogue.",
            "Kat isn't judging the maid. Kat is judging the fucking degenerates in the audience.",
        ],
    },

    "ntr": {
        "emoji": [
            "💀",
        ],
        "messages": [
            "Oh, fuck off. We're taking the cursed route today, apparently.",
            "Right. That's enough internet for one fucking day. Somebody queue the wholesome anime.",
            "What the actual fuck did I just read? Even the background NPCs are uncomfortable.",
            "Brilliant. We've entered the dark arc. Somebody call the protagonist.",
            "Nope. Kat is skipping this episode. We've already seen enough character development.",
            "We've crossed into the part of the fandom nobody explains to the normies.",
            "Who the fuck opened the forbidden anime folder?",
            "Kat has officially declared this conversation non-canon. Moving on.",
        ],
    },

    "bunny_suit": {
        "emoji": [
            "👯‍♀️",
        ],
        "messages": [
            "A bunny suit. Naturally. We've reached peak anime convention behavior.",
            "Well, there goes the last shred of dignity. Somebody get the cosplay camera.",
            "Someone saw a bunny suit and immediately activated their inner anime protagonist.",
            "Christ alive. You lot are one seasonal anime away from becoming full-time weebs.",
            "Bunny suit detected. Brain cells have left the chat. Probably watching anime somewhere.",
            "Ah yes, the legendary bunny girl. An ancient anime spell known to destroy everyone's composure.",
            "Kat has questions. Unfortunately, every possible answer makes this conversation worse.",
            "Right. Keep staring at the fictional woman. I'm sure the plot is very important.",
        ],
    },

    "australia": {
        "emoji": [
            "🦘",
        ],
        "messages": [
            "Australia mentioned. Fucking hell, the final boss has entered the server.",
            "An Aussie? Right. Hide the beer, secure the wildlife, and don't make eye contact.",
            "G'day, you bloody anime protagonist. Try not to start a side quest.",
            "Australia mentioned. Somewhere, a kangaroo just gained +10 STR.",
            "Ah yes, Australia. The real-life isekai where everything wants to fucking kill you.",
            "Aussie detected. Probability of chaotic protagonist behavior has increased dramatically.",
            "Oz, mate. Absolutely fucking feral. I respect the character design.",
            "Right, who's summoned the Australian? Was this part of the plot or did we just unlock a secret route?",
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

def contains_keyword(text: str, keyword: str) -> bool:
    return re.search(
        rf"\b{re.escape(keyword)}\b",
        text,
    ) is not None

def get_reaction(message_content: str):
    text = message_content.lower()

    if any(
        contains_keyword(text, word)
        for word in (
            "magical girl",
            "magic girl",
            "madoka",
        )
    ):
        category = "magical_girl"

    elif any(
        contains_keyword(text, word)
        for word in (
            "bunny suit",
            "bunny girl",
        )
    ):
        category = "bunny_suit"

    elif any(
        contains_keyword(text, word)
        for word in (
            "ntr",
            "netorare",
        )
    ):
        category = "ntr"

    elif any(
        contains_keyword(text, word)
        for word in (
            "maido",
            "maid",
        )
    ):
        category = "maid"

    elif any(
        contains_keyword(text, word)
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