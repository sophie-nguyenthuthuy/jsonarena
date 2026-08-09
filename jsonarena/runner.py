"""Benchmark runner: correctness gate first, then timed parse/serialize."""
from __future__ import annotations

import json
import math
import platform
import statistics
import sys
import time
from datetime import datetime, timezone
from typing import Any

from . import datasets
from .adapters import AdapterError, resolve
from .entry import Entry

# ujson caps float output at 10 significant digits by default; datasets use
# ≤9-digit floats so this tolerance is generous headroom, not a fudge factor.
_REL_TOL = 1e-9
_ABS_TOL = 1e-12


def deep_eq(a: Any, b: Any) -> bool:
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(deep_eq(a[k], b[k]) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(deep_eq(x, y) for x, y in zip(a, b))
    # bool is an int subclass — don't let True == 1 pass
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=_REL_TOL, abs_tol=_ABS_TOL)
    return a == b


def check_correctness(mod, raw: bytes, canonical: Any) -> str | None:
    """Return an error string, or None if the adapter round-trips faithfully."""
    try:
        parsed = mod.loads(raw)
    except Exception as e:
        return f"loads raised {type(e).__name__}: {e}"
    if not deep_eq(parsed, canonical):
        return "loads output differs from stdlib parse"
    try:
        out = mod.dumps(canonical)
    except Exception as e:
        return f"dumps raised {type(e).__name__}: {e}"
    try:
        reparsed = json.loads(out)
    except Exception as e:
        return f"dumps output is not valid JSON: {e}"
    if not deep_eq(reparsed, canonical):
        return "dumps round-trip differs from original"
    return None


def _time_op(fn, arg, repeats: int, warmup: int = 2) -> float:
    """Median wall time of fn(arg) in seconds."""
    for _ in range(warmup):
        fn(arg)
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        fn(arg)
        times.append(time.perf_counter_ns() - t0)
    return statistics.median(times) / 1e9


def run(entries: list[Entry], repeats: int = 10) -> dict:
    data = datasets.build()
    canonical = {name: json.loads(raw) for name, raw in data.items()}
    result: dict = {
        "meta": {
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "python": platform.python_version(),
            "platform": f"{platform.system()} {platform.machine()}",
            "repeats": repeats,
        },
        "datasets": {name: {"bytes": len(raw)} for name, raw in data.items()},
        "libraries": [],
    }
    for entry in entries:
        row: dict = {
            "name": entry.name,
            "repo": entry.repo,
            "language": entry.language,
            "baseline": entry.baseline,
        }
        try:
            mod = resolve(entry.adapter)
            row["version"] = mod.version()
        except AdapterError as e:
            row["status"] = "unavailable"
            row["error"] = str(e)
            result["libraries"].append(row)
            print(f"  SKIP {entry.name}: {e}", file=sys.stderr)
            continue

        row["benchmarks"] = {}
        errors = []
        for ds_name, raw in data.items():
            err = check_correctness(mod, raw, canonical[ds_name])
            if err:
                errors.append(f"{ds_name}: {err}")
                continue
            row["benchmarks"][ds_name] = {
                "parse_s": _time_op(mod.loads, raw, repeats),
                "serialize_s": _time_op(mod.dumps, canonical[ds_name], repeats),
            }
        if errors:
            row["status"] = "failed-correctness"
            row["error"] = "; ".join(errors)
        else:
            row["status"] = "ok"
        result["libraries"].append(row)
        print(f"  {row['status']:>6}  {entry.name} {row.get('version', '')}", file=sys.stderr)
    return result
