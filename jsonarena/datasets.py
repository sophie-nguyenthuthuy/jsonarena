"""Deterministic synthetic JSON datasets.

Generated from a fixed seed at bench time, so the repo carries no large
fixtures and every run (local or CI) benchmarks identical payloads.
Floats are finite and rounded to 6 decimals so strict encoders (orjson)
accept them and round-trips stay within tolerance for every library.
"""
from __future__ import annotations

import json
import random
import string

SEED = 20260809

_ASCII = string.ascii_letters + string.digits
_VIET = (
    "aăâbcdđeêghiklmnoôơpqrstuưvxy"
    "àáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩị"
    "òóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ "
)


def _word(rng: random.Random, alphabet: str, lo: int = 3, hi: int = 12) -> str:
    return "".join(rng.choice(alphabet) for _ in range(rng.randint(lo, hi)))


def _numbers(rng: random.Random) -> object:
    """Float/int heavy — coordinates-style payload (canada.json analogue)."""
    return {
        "coordinates": [
            [round(rng.uniform(-180, 180), 6), round(rng.uniform(-90, 90), 6)]
            for _ in range(30_000)
        ],
        "ids": [rng.randrange(10**9) for _ in range(10_000)],
    }


def _structs(rng: random.Random) -> object:
    """Uniform array of records — API-response-style payload (twitter.json analogue)."""
    return [
        {
            "id": i,
            "user": _word(rng, _ASCII, 6, 14),
            "active": rng.random() < 0.5,
            "score": round(rng.uniform(0, 100), 6),
            "tags": [_word(rng, _ASCII, 3, 8) for _ in range(rng.randint(0, 4))],
            "meta": {"lang": rng.choice(["vi", "en", "ja"]), "rank": rng.randrange(1000)},
        }
        for i in range(6_000)
    ]


def _strings(rng: random.Random) -> object:
    """Unicode-heavy — Vietnamese text, exercises escaping and UTF-8 paths."""
    return [
        " ".join(_word(rng, _VIET, 2, 8) for _ in range(rng.randint(5, 20)))
        for _ in range(4_000)
    ]


def _mixed(rng: random.Random) -> object:
    """Nested heterogeneous tree — worst case for branchy parsers."""
    def node(depth: int) -> object:
        if depth == 0 or rng.random() < 0.3:
            return rng.choice(
                [
                    rng.randrange(10**6),
                    round(rng.uniform(-1000, 1000), 6),
                    _word(rng, _ASCII),
                    rng.random() < 0.5,
                    None,
                ]
            )
        if rng.random() < 0.5:
            return [node(depth - 1) for _ in range(rng.randint(1, 6))]
        return {_word(rng, _ASCII, 3, 8): node(depth - 1) for _ in range(rng.randint(1, 6))}

    return [node(6) for _ in range(1_200)]


_GENERATORS = {
    "numbers": _numbers,
    "structs": _structs,
    "strings": _strings,
    "mixed": _mixed,
}


def build() -> dict[str, bytes]:
    """name -> canonical UTF-8 JSON bytes (stdlib-encoded, ensure_ascii=False)."""
    out: dict[str, bytes] = {}
    for name, gen in _GENERATORS.items():
        obj = gen(random.Random(f"{SEED}:{name}"))
        out[name] = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode()
    return out
