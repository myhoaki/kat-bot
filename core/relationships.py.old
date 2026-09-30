import hashlib
import json
import os
import random
import time


DATA_FOLDER = "/app/data"
RELATIONSHIP_FILE = os.path.join(
    DATA_FOLDER,
    "relationships.json",
)

# Relationship action cooldown.
RELATIONSHIP_COOLDOWN = 30

# Stores the last time each user used
# a relationship-changing action.
relationship_cooldowns = {}


os.makedirs(DATA_FOLDER, exist_ok=True)


def load_relationships():
    if not os.path.exists(RELATIONSHIP_FILE):
        return {}

    try:
        with open(
            RELATIONSHIP_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return {}


def save_relationships(data):
    with open(
        RELATIONSHIP_FILE,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=4,
        )


relationships = load_relationships()


def get_pair_key(user1_id, user2_id):
    pair = tuple(
        sorted(
            [
                str(user1_id),
                str(user2_id),
            ]
        )
    )

    return f"{pair[0]}:{pair[1]}"


def generate_relationship(
    user1_id,
    user2_id,
):
    pair_key = get_pair_key(
        user1_id,
        user2_id,
    )

    if pair_key in relationships:
        return relationships[pair_key]

    pair = tuple(
        pair_key.split(":")
    )

    seed_string = (
        f"{pair[0]}-{pair[1]}"
    )

    seed = int(
        hashlib.sha256(
            seed_string.encode()
        ).hexdigest(),
        16,
    )

    rng = random.Random(seed)

    stats = {
        "romance": rng.randint(0, 100),
        "friendship": rng.randint(0, 100),
        "chemistry": rng.randint(0, 100),
        "chaos": rng.randint(0, 100),
        "kat_approval": rng.randint(0, 100),
    }

    relationships[pair_key] = stats

    save_relationships(relationships)

    return stats


def get_relationship_cooldown_remaining(
    user_id,
):
    last_used = relationship_cooldowns.get(
        user_id,
        0,
    )

    remaining = (
        RELATIONSHIP_COOLDOWN
        - (time.monotonic() - last_used)
    )

    return max(0, remaining)


def start_relationship_cooldown(
    user_id,
):
    relationship_cooldowns[user_id] = (
        time.monotonic()
    )


def apply_relationship_change(
    user1_id,
    user2_id,
    changes,
):
    """
    Apply random relationship changes.

    Each change is defined as:

        "friendship": (-3, 8)

    meaning the stat can randomly change
    anywhere from -3 to +8.
    """

    stats = generate_relationship(
        user1_id,
        user2_id,
    )

    actual_changes = {}

    for stat, change_range in changes.items():
        if stat not in stats:
            continue

        minimum, maximum = change_range

        change = random.randint(
            minimum,
            maximum,
        )

        old_value = stats[stat]

        new_value = max(
            0,
            min(
                100,
                old_value + change,
            ),
        )

        stats[stat] = new_value

        actual_changes[stat] = (
            new_value - old_value
        )

    save_relationships(relationships)

    return stats, actual_changes


def apply_action_relationship(
    user1_id,
    user2_id,
    action,
):
    """
    Apply an RNG-based relationship effect
    for one of Kat's interaction commands.
    """

    action_effects = {
        "hug": {
            "friendship": (-2, 8),
            "romance": (-1, 5),
            "chemistry": (0, 6),
        },

        "kiss": {
            "romance": (2, 10),
            "chemistry": (1, 8),
            "friendship": (-2, 4),
        },

        "pat": {
            "friendship": (1, 7),
            "romance": (-2, 3),
            "chemistry": (-1, 4),
        },

        "cuddle": {
            "friendship": (2, 9),
            "romance": (2, 8),
            "chemistry": (1, 7),
        },

        "highfive": {
            "friendship": (1, 6),
            "chemistry": (1, 5),
            "chaos": (-2, 3),
        },

        "slap": {
            "friendship": (-10, -2),
            "chemistry": (-3, 4),
            "chaos": (3, 10),
            "kat_approval": (-5, 2),
        },

        "preg": {
            "romance": (-5, 10),
            "friendship": (-4, 6),
            "chemistry": (-3, 10),
            "chaos": (5, 15),
            "kat_approval": (-10, 5),
        },
    }

    changes = action_effects.get(action)

    if not changes:
        return (
            generate_relationship(
                user1_id,
                user2_id,
            ),
            {},
        )

    return apply_relationship_change(
        user1_id,
        user2_id,
        changes,
    )


def relationship_verdict(stats):
    score = (
        stats["romance"]
        + stats["friendship"]
        + stats["chemistry"]
    ) / 3

    if score >= 90:
        return "GET A ROOM. 💀"

    if score >= 80:
        return (
            "Kat is extremely suspicious "
            "of this relationship. 👀"
        )

    if score >= 70:
        return (
            "Okay, this is getting suspicious. 😳"
        )

    if score >= 60:
        return (
            "There is definitely something "
            "going on here."
        )

    if score >= 45:
        return (
            "There is potential... maybe."
        )

    if score >= 30:
        return (
            "You two have met. That's about it. 💀"
        )

    return (
        "Kat recommends staying "
        "50 meters apart. 🚨"
    )


def kat_relationship_reaction(stats):
    romance = stats["romance"]
    friendship = stats["friendship"]
    chemistry = stats["chemistry"]
    chaos = stats["chaos"]
    kat_approval = stats["kat_approval"]

    if romance >= 80 and chemistry >= 80:
        return (
            "GET A FUCKING ROOM. "
            "I'm not watching this shit. 💀"
        )

    if friendship >= 80 and romance <= 30:
        return (
            "Bestie territory. "
            "Don't make this weird. 🤝"
        )

    if chaos >= 85:
        return (
            "You two are a public safety hazard. "
            "Kat is concerned. 🚨"
        )

    if kat_approval >= 80:
        return (
            "Kat approves. Somehow. "
            "Don't fuck it up. 🐱"
        )

    if kat_approval <= 20:
        return (
            "Kat has serious concerns about this "
            "entire fucking situation. 👀"
        )

    if friendship >= 70 and chemistry >= 70:
        return (
            "There's definitely something here. "
            "I'm not saying what. 👀"
        )

    return (
        "Kat needs more evidence before passing "
        "judgment. Keep going, I guess."
    )
