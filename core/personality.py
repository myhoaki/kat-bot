import random


KAT_EMOJI = "<:giga_mpreg:1512315959279353986>"


REACTIONS = {
    "hug": [
        "Aww. Disgusting. I approve. 🐱",
        "Look at you two being wholesome. Gross. ❤️",
        "Fine. You may have one wholesome moment.",
        "Kat has witnessed affection. Kat will pretend she didn't.",
        "Hugs? In THIS economy? 🥹",
    ],
    "kiss": [
        "OH? 👀",
        "Kat saw that. Don't even try denying it.",
        "Interesting. Very interesting. 🐱",
        "Someone's feeling brave today. 💀",
        "I am looking respectfully. 👀",
    ],
    "pat": [
        "Pat received. Dignity slightly damaged. 🐱",
        "There there. Good human.",
        "Kat approves this level of affection.",
        "Pat pat. You may continue existing.",
    ],
    "slap": [
        "Excellent technique. 💀",
        "Kat would like to see that again.",
        "Violence? In MY server? Incredible.",
        "That was personal. I respect it.",
        "Absolutely unnecessary. Do it again.",
    ],
    "cuddle": [
        "Fine. Everyone gets one cuddle. ONE.",
        "Kat approves the emotional support.",
        "Wholesome detected. Deploying approval. ❤️",
        "You two are making this server suspiciously cute.",
    ],
    "highfive": [
        "LET'S GOOOOO 🙌",
        "Kat approves. Solid teamwork.",
        "High five accepted. +10 aura.",
        "Finally. Someone with good instincts.",
    ],
    "preg": [
        "💀 Kat is choosing not to ask questions.",
        "Bro WHAT.",
        "Kat has concerns.",
        "I am not emotionally prepared for this.",
        "Absolutely cursed behavior. 💀",
    ],
}


MOODS = [
    "😎 effortlessly cool",
    "🐱 mildly judgmental",
    "💀 one bad idea away from disaster",
    "👀 watching everyone's business",
    "❤️ secretly wholesome",
    "🔥 feeling unnecessarily powerful",
    "🧠 pretending to know what she's doing",
    "😈 looking for chaos",
]


ROASTS = [
    "{user}, your Wi-Fi signal has more personality than you do. 💀",
    "{user}, Kat has seen your search history. We need to talk. 👀",
    "{user}, you're not the main character. You're barely DLC. 💀",
    "{user}, somehow you managed to lower the server's IQ. Impressive.",
    "{user}, Kat would roast you harder, but she's trying to be nice today. 😌",
    "{user}, your aura is currently buffering...",
    "{user}, I've seen NPCs with more character development.",
    "{user}, you bring a very special energy to this server. Unfortunately.",
]


COMPLIMENTS = [
    "{user}, you're actually pretty cool. Don't let it go to your head. 😎",
    "{user}, Kat officially approves of you. This is extremely rare. 🐱",
    "{user}, you've got good vibes. Suspiciously good vibes. 👀",
    "{user}, you're one of the few people Kat would trust with the aux.",
    "{user}, okay fine... you're kinda awesome. ❤️",
    "{user}, certified good human. For now.",
]


JUDGMENTS = [
    "Kat has reviewed the evidence. The vibes are suspicious. 👀",
    "Hmm... questionable behavior detected.",
    "Kat's professional opinion: you are probably responsible.",
    "I've decided you're guilty. I don't know of what yet. 💀",
    "The council has deliberated. Kat was the only council member.",
    "Your vibes have been inspected. Results are classified.",
    "Kat has no evidence, but she has a feeling. That's enough.",
]


WISDOM = [
    "Never trust someone who says 'trust me.' 🐱",
    "If it works, it works. If it doesn't, blame the Wi-Fi.",
    "Always bring snacks to important meetings. 🍪",
    "Life is short. Cause minor chaos.",
    "If you don't know what you're doing, act confident. 😎",
    "Sometimes the best solution is to make it someone else's problem.",
    "Protect your peace. And your snacks.",
    "Kat knows the answer. Kat will not be explaining.",
]


CHAOS = [
    "I have an idea. It is a terrible one. 😈",
    "Everyone remain calm. I have absolutely no plan.",
    "What if we made this situation significantly worse? 💀",
    "Kat has pressed the mysterious button.",
    "This server needs more chaos. Obviously.",
    "I could fix this. I could also make it 10x worse.",
    "Something is about to happen. I will not elaborate. 👀",
]


def random_reaction(action: str) -> str:
    messages = REACTIONS.get(
        action,
        ["Kat has no comment. 🐱"],
    )

    return random.choice(messages)


def random_mood() -> str:
    return random.choice(MOODS)


def random_roast(user) -> str:
    return random.choice(ROASTS).format(
        user=user.mention
    )


def random_compliment(user) -> str:
    return random.choice(COMPLIMENTS).format(
        user=user.mention
    )


def random_judgment() -> str:
    return random.choice(JUDGMENTS)


def random_wisdom() -> str:
    return random.choice(WISDOM)


def random_chaos() -> str:
    return random.choice(CHAOS)
