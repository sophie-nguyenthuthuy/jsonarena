"""Entry files: one TOML per benchmarked library under entries/."""
from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

_ADAPTER_RE = re.compile(r"^[a-zA-Z_][\w.]*$")
_REQUIRED = ("name", "adapter", "repo")


class EntryError(ValueError):
    pass


@dataclass(frozen=True)
class Entry:
    name: str
    adapter: str          # importable module exposing loads/dumps/version
    repo: str
    package: str = ""     # pip install target; empty = nothing to install (stdlib)
    language: str = ""    # implementation language of the hot path
    notes: str = ""
    baseline: bool = False
    source: Path | None = field(default=None, compare=False)


def load_entry(path: Path) -> Entry:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as e:
        raise EntryError(f"{path.name}: invalid TOML: {e}") from e
    missing = [k for k in _REQUIRED if not data.get(k)]
    if missing:
        raise EntryError(f"{path.name}: missing required field(s): {', '.join(missing)}")
    unknown = set(data) - {"name", "adapter", "repo", "package", "language", "notes", "baseline"}
    if unknown:
        raise EntryError(f"{path.name}: unknown field(s): {', '.join(sorted(unknown))}")
    if not _ADAPTER_RE.match(data["adapter"]):
        raise EntryError(f"{path.name}: adapter is not a valid module path: {data['adapter']!r}")
    if not data["repo"].startswith("https://"):
        raise EntryError(f"{path.name}: repo must be an https URL")
    return Entry(source=path, **data)


def load_entries(dirpath: Path) -> list[Entry]:
    entries = [load_entry(p) for p in sorted(dirpath.glob("*.toml"))]
    if not entries:
        raise EntryError(f"no entries found in {dirpath}")
    names = [e.name for e in entries]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise EntryError(f"duplicate entry name(s): {', '.join(sorted(dupes))}")
    baselines = [e for e in entries if e.baseline]
    if len(baselines) != 1:
        raise EntryError(f"exactly one entry must set baseline = true (found {len(baselines)})")
    return entries
