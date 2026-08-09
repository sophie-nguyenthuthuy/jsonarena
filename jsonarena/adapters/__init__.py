"""Adapter contract: a module exposing

    loads(data: bytes) -> object
    dumps(obj) -> bytes | str
    version() -> str

Keep adapters thin — no tuning flags that wouldn't be a library's
documented default. The bench measures defaults, not hand-tuned modes.
"""
from __future__ import annotations

import importlib
from types import ModuleType

_CONTRACT = ("loads", "dumps", "version")


class AdapterError(RuntimeError):
    pass


def resolve(module_path: str) -> ModuleType:
    try:
        mod = importlib.import_module(module_path)
    except ImportError as e:
        raise AdapterError(f"cannot import {module_path}: {e}") from e
    missing = [a for a in _CONTRACT if not callable(getattr(mod, a, None))]
    if missing:
        raise AdapterError(f"{module_path} missing callable(s): {', '.join(missing)}")
    return mod
