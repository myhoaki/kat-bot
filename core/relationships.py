import hashlib
import json
import os
import random


DATA_FOLDER = "/app/data"
RELATIONSHIP_FILE = os.path.join(
    DATA_FOLDER,
    "relationships.json",
)

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


def generate_relationship(
    user1_id,
    user2_id,
):
    pair = tuple(
        sorted(
            [
                str(user1_id),
                str(user2_id),
            ]
        )
    )

    pair_key = f"{pair[0]}:{pair[1]}"

    if pair_key in relationships:
        return relationships[pair_key]

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