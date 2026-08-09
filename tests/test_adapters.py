"""Contract + correctness for every entry whose package is installed.

Uninstalled third-party libraries are skipped (local dev may not have all
wheels); CI installs everything via `jsonarena deps`, so nothing skips there.
"""
import json

import pytest

from jsonarena.adapters import AdapterError, resolve
from jsonarena.cli import ROOT
from jsonarena.entry import load_entries
from jsonarena.runner import check_correctness, deep_eq

ENTRIES = load_entries(ROOT / "entries")
SAMPLE = {"vi": "Hà Nội ơi", "n": [1, 2.5, -3], "ok": True, "none": None, "nest": {"a": [{}]}}
SAMPLE_RAW = json.dumps(SAMPLE, ensure_ascii=False).encode()


def _mod(entry):
    try:
        return resolve(entry.adapter)
    except AdapterError:
        pytest.skip(f"{entry.name} not installed")


@pytest.mark.parametrize("entry", ENTRIES, ids=lambda e: e.name)
def test_contract(entry):
    mod = _mod(entry)
    assert isinstance(mod.version(), str) and mod.version()
    assert mod.loads(SAMPLE_RAW) == SAMPLE
    out = mod.dumps(SAMPLE)
    assert isinstance(out, (str, bytes))
    assert json.loads(out) == SAMPLE


@pytest.mark.parametrize("entry", ENTRIES, ids=lambda e: e.name)
def test_correctness_gate_passes(entry):
    mod = _mod(entry)
    err = check_correctness(mod, SAMPLE_RAW, SAMPLE)
    assert err is None, err


def test_deep_eq_catches_type_confusion():
    assert not deep_eq(True, 1)
    assert not deep_eq([1], [1, 1])
    assert not deep_eq({"a": 1}, {"b": 1})
    assert deep_eq(0.1 + 0.2, 0.3)  # within tolerance
    assert not deep_eq(1.0, 1.1)


def test_correctness_gate_catches_lossy_library():
    class Lossy:
        @staticmethod
        def loads(b):
            return json.loads(b)

        @staticmethod
        def dumps(o):
            return json.dumps(o).replace("2.5", "2.4")

        @staticmethod
        def version():
            return "0"

    assert check_correctness(Lossy, SAMPLE_RAW, SAMPLE) is not None
