import json

from jsonarena import datasets


def test_deterministic():
    assert datasets.build() == datasets.build()


def test_all_datasets_valid_json_and_nontrivial():
    data = datasets.build()
    assert set(data) == {"numbers", "structs", "strings", "mixed"}
    for name, raw in data.items():
        obj = json.loads(raw)
        assert obj, name
        assert len(raw) > 100_000, f"{name} too small to benchmark meaningfully"


def test_floats_are_finite():
    # orjson rejects NaN/Infinity; datasets must never contain them
    import math

    def walk(o):
        if isinstance(o, float):
            assert math.isfinite(o)
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for raw in datasets.build().values():
        walk(json.loads(raw))
