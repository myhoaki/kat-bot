import random


KAT_EMOJI = "<:giga_mpreg:1512315959279353986>"


REACTIONS = {
    "hug": [
        "Oh, look at that. Two people showing affection. Fucking revolting. Carry on.",
        "Go on then, have your little cuddle. Christ knows we need some decent behavior around here.",
        "Well, would you look at that. Something wholesome for once. Don't make a habit of it.",
        "Jesus Christ, you're actually being nice to each other. I'm almost disappointed.",
        "A hug? Bloody hell. Someone's gone soft.",
        "Fine. Have your fucking hug. Just keep the emotional speeches to yourself.",
        "That's actually rather sweet. Don't tell anyone I said that.",
        "Look at you two. Being wholesome like a pair of fucking lunatics.",
    ],

    "kiss": [
        "Oh, here we fucking go. Someone's making moves.",
        "Right. I saw that. Don't pretend you didn't fucking mean it.",
        "Well, that's one way to make things interesting.",
        "Christ alive. Get a room, you pair of degenerates.",
        "Oh? Someone's feeling brave. I respect the fucking audacity.",
        "Right, noted. Kat's keeping an eye on this situation.",
        "That was either incredibly romantic or incredibly fucking stupid.",
        "Carry on. This is better entertainment than television.",
    ],

    "pat": [
        "There, there. Good human. Now piss off and behave yourself.",
        "Pat received. Dignity reduced by approximately 40 percent.",
        "Go on then. You've earned it. Don't fucking get greedy.",
        "Pat pat. Christ, we're all a bit pathetic sometimes.",
        "There you go. Emotional support delivered. You're welcome.",
        "A head pat? Fine. I'll allow it.",
        "Look at you. Getting praised for simply existing. Bloody marvelous.",
    ],

    "slap": [
        "Jesus fucking Christ. Straight to violence.",
        "Excellent. A completely reasonable response to whatever the hell happened.",
        "Well, that escalated fucking quickly.",
        "That was personal. I respect the fucking commitment.",
        "Absolutely unnecessary. Do it again.",
        "Christ. Someone woke up choosing violence.",
        "Right. We're solving problems with our hands now. Brilliant.",
        "That slap had more conviction than most people's life choices.",
    ],

    "cuddle": [
        "Fine. One cuddle. Don't push your fucking luck.",
        "Oh for fuck's sake, we're being wholesome again.",
        "Emotional support deployed. Try not to make this weird.",
        "Look at you two. Disgustingly adorable.",
        "Christ alive, get a room. Or don't. I'm not your fucking mother.",
        "Fine. Cuddle away. The world is miserable enough as it is.",
        "That's actually rather nice. Bloody hell, don't make me say it twice.",
    ],

    "highfive": [
        "Fucking hell, finally. Someone with good instincts.",
        "Now that's what I'm fucking talking about.",
        "High five accepted. Try not to fuck it up.",
        "Solid work. Kat approves. Don't let it go to your head.",
        "Beautiful. Absolutely fucking beautiful.",
        "That's the spirit. Now let's go cause some trouble.",
        "Finally, a competent fucking interaction.",
    ],

    "preg": [
        "What the actual fuck.",
        "Christ alive. Kat has questions, and frankly, she's afraid of the answers.",
        "Right. We're just doing this now, apparently.",
        "How the fuck did we get here?",
        "Absolutely fucking cursed. I need a drink.",
        "Jesus Christ. Someone explain this shit.",
        "Nope. Not asking. Some mysteries are better left fucking mysterious.",
        "This server continues to find new ways to disappoint me.",
    ],
}


MOODS = [
    "😎 cool as fucking ice",
    "🐱 profoundly unimpressed with everyone's bullshit",
    "💀 one bad decision away from absolute fucking disaster",
    "👀 watching everyone's business like it's premium television",
    "❤️ secretly wholesome, which is frankly fucking embarrassing",
    "🔥 feeling dangerously confident",
    "🧠 pretending she has a fucking plan",
    "😈 looking for trouble because apparently peace is boring",
    "☕ tired of everyone's shit",
    "💀 wondering why she's surrounded by fucking idiots",
    "😐 emotionally unavailable but still somehow invested",
    "🔪 calm, collected, and probably a terrible influence",
]


ROASTS = [
    "{user}, your Wi-Fi signal has more personality than you do. Fucking tragic.",
    "{user}, I've seen roadkill with better decision-making skills.",
    "{user}, you're not the main character. You're barely fucking DLC.",
    "{user}, somehow you've managed to lower the collective IQ of the server.",
    "{user}, Kat could roast you harder, but life's already doing a pretty solid fucking job.",
    "{user}, your aura isn't buffering. It's fucking dead.",
    "{user}, I've seen NPCs with more character development.",
    "{user}, you bring a very special energy to this server. Unfortunately.",
    "{user}, if bad decisions were a profession, you'd be fucking management.",
    "{user}, I've got nothing against you. You're just remarkably easy to fucking mock.",
    "{user}, you're proof that confidence and competence are completely unrelated.",
    "{user}, you've got the confidence of someone who's never been told to shut the fuck up.",
    "{user}, I'd explain why you're wrong, but I don't have the fucking patience.",
    "{user}, you're not useless. You make everyone else feel better about themselves.",
    "{user}, Christ, I've seen smarter decisions made by a fucking coin toss.",
    "{user}, somewhere along the way, common sense took one look at you and fucking resigned.",
]


COMPLIMENTS = [
    "{user}, you're actually pretty fucking cool. Don't let it go to your head.",
    "{user}, Kat officially approves of you. Don't make her regret it.",
    "{user}, you've got good vibes. Suspiciously good vibes.",
    "{user}, you're one of the few people Kat would trust with the aux.",
    "{user}, alright, fine. You're fucking awesome. Happy now?",
    "{user}, certified good human. Against all fucking odds.",
    "{user}, you've got your shit together. Kat respects that.",
    "{user}, you're alright. That's a surprisingly high compliment coming from me.",
    "{user}, Kat hates admitting it, but you're actually pretty solid.",
    "{user}, you're doing alright. Keep your head up and don't let the bastards get you down.",
    "{user}, you've earned Kat's respect. That's worth more than whatever bullshit trophy you've got.",
    "{user}, not bad. You've actually got some fucking character.",
]


JUDGMENTS = [
    "I've reviewed the evidence. You're suspicious as fuck.",
    "Hmm. That's questionable behavior, mate.",
    "Professional assessment: you're probably responsible.",
    "I've decided you're guilty. I haven't decided of what yet.",
    "The council has deliberated. The council was me. You're fucked.",
    "Your vibes have been inspected. Results are fucking concerning.",
    "I've got no evidence, but I've got a feeling. That's good enough.",
    "After careful consideration: fucking suspicious.",
    "The evidence is circumstantial. The judgment is not.",
    "Verdict: probably a menace.",
    "I've seen enough. You're trouble.",
    "Something about you screams 'bad fucking idea.'",
    "I'm not saying you're guilty. I'm saying I wouldn't trust you with the keys.",
]


WISDOM = [
    "Never trust someone who says 'trust me.' They're usually full of shit.",
    "If it works, it works. If it doesn't, blame the fucking Wi-Fi.",
    "Always bring snacks. Starving people make terrible decisions.",
    "Life is short. Cause a little fucking chaos.",
    "If you don't know what you're doing, act confident. Works surprisingly well.",
    "Sometimes the best solution is making it someone else's fucking problem.",
    "Protect your peace. And your fucking snacks.",
    "I know the answer. I'm just not explaining it. Figure it out.",
    "Never make an important decision while hungry or horny. Preferably neither.",
    "If someone says 'this can't possibly get worse,' it absolutely fucking can.",
    "When in doubt, pretend it was intentional.",
    "Common sense is apparently a fucking premium feature.",
    "Trust your instincts. Unless your instincts are shit.",
    "Don't start a fight you can't finish. Unless it's funny. Then reconsider.",
    "Sometimes you've just got to say 'fuck it' and see what happens.",
    "Keep your friends close and your snacks closer.",
]


CHAOS = [
    "I've got an idea. It's fucking terrible. Let's do it.",
    "Everyone remain calm. I've absolutely no fucking plan.",
    "What if we made this situation significantly worse? Just asking.",
    "I've pressed the mysterious button. No fucking refunds.",
    "This server needs more chaos. Obviously.",
    "I could fix this. I could also make it ten times fucking worse.",
    "Something's about to happen. I'm accepting no fucking responsibility.",
    "Right. Fuck it. Let's see what happens.",
    "I have no idea what I'm doing, and somehow that's never stopped me before.",
    "We've come too far to turn back now. Probably.",
    "I've made a decision. It was the wrong one. Let's fucking commit.",
    "This is either going to be brilliant or an absolute fucking disaster.",
    "Nobody panic. Actually, fuck that. Panic.",
    "I see the problem. I have chosen to make it worse.",
    "We've got two options: behave ourselves or make this fucking interesting.",
]


def random_reaction(action: str) -> str:
    messages = REACTIONS.get(
        action,
        ["Kat has no fucking comment."],
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