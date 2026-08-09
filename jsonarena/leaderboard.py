"""Render the README leaderboard (and RESULTS.md breakdown) from results JSON."""
from __future__ import annotations

import math
import re
from pathlib import Path

START = "<!-- LEADERBOARD:START -->"
END = "<!-- LEADERBOARD:END -->"

_MEDALS = {1: "🥇", 2: "🥈", 3: "🥉"}


def _geomean(xs: list[float]) -> float:
    return math.exp(sum(math.log(x) for x in xs) / len(xs))


def _throughputs(lib: dict, results: dict) -> tuple[float, float]:
    """Geo-mean MB/s across datasets for (parse, serialize).

    MB/s uses the canonical payload size for both ops so serialize numbers
    are comparable across libraries with different output compactness.
    """
    parse, ser = [], []
    for ds_name, bench in lib["benchmarks"].items():
        size_mb = results["datasets"][ds_name]["bytes"] / 1e6
        parse.append(size_mb / bench["parse_s"])
        ser.append(size_mb / bench["serialize_s"])
    return _geomean(parse), _geomean(ser)


def rank(results: dict) -> list[dict]:
    """Scored rows for status=ok libraries, sorted best-first."""
    baseline = next(
        (l for l in results["libraries"] if l.get("baseline") and l.get("status") == "ok"),
        None,
    )
    if baseline is None:
        raise RuntimeError("baseline library missing or not ok — cannot compute relative scores")
    base_parse, base_ser = _throughputs(baseline, results)
    rows = []
    for lib in results["libraries"]:
        if lib.get("status") != "ok":
            continue
        parse, ser = _throughputs(lib, results)
        rows.append(
            {
                "name": lib["name"],
                "repo": lib["repo"],
                "version": lib.get("version", ""),
                "language": lib.get("language", ""),
                "parse_mbs": parse,
                "serialize_mbs": ser,
                "parse_x": parse / base_parse,
                "serialize_x": ser / base_ser,
                "overall_x": _geomean([parse / base_parse, ser / base_ser]),
            }
        )
    rows.sort(key=lambda r: r["overall_x"], reverse=True)
    return rows


def render_table(results: dict) -> str:
    rows = rank(results)
    meta = results["meta"]
    lines = [
        "| Rank | Library | Version | Lang | Parse | Serialize | Overall |",
        "|-----:|---------|---------|------|------:|----------:|--------:|",
    ]
    for i, r in enumerate(rows, 1):
        medal = _MEDALS.get(i, str(i))
        lines.append(
            f"| {medal} | [{r['name']}]({r['repo']}) | {r['version']} | {r['language']} "
            f"| {r['parse_x']:.2f}× | {r['serialize_x']:.2f}× | **{r['overall_x']:.2f}×** |"
        )
    excluded = [l for l in results["libraries"] if l.get("status") not in (None, "ok")]
    if any(l["status"] != "ok" for l in excluded):
        lines.append("")
        for l in excluded:
            if l["status"] != "ok":
                lines.append(f"- ⚠️ **{l['name']}** excluded ({l['status']}): {l.get('error', '')}")
    lines += [
        "",
        f"*Speed relative to the stdlib baseline (higher is better), geometric mean over "
        f"{len(results['datasets'])} datasets. "
        f"Python {meta['python']}, {meta['platform']}, {meta['timestamp']}. "
        f"Full numbers in [RESULTS.md](RESULTS.md).*",
    ]
    return "\n".join(lines)


def render_results_md(results: dict) -> str:
    meta = results["meta"]
    out = [
        "# Full results",
        "",
        f"Python {meta['python']} · {meta['platform']} · {meta['timestamp']} · "
        f"median of {meta['repeats']} runs",
        "",
        "## Datasets",
        "",
        "| Dataset | Size |",
        "|---------|-----:|",
    ]
    for name, ds in results["datasets"].items():
        out.append(f"| {name} | {ds['bytes'] / 1e6:.2f} MB |")
    for op, key in (("Parse", "parse_s"), ("Serialize", "serialize_s")):
        out += ["", f"## {op} (ms, lower is better)", ""]
        header = "| Library | " + " | ".join(results["datasets"]) + " |"
        out += [header, "|---------|" + "---:|" * len(results["datasets"])]
        for lib in results["libraries"]:
            if lib.get("status") != "ok":
                continue
            cells = [
                f"{lib['benchmarks'][ds][key] * 1000:.2f}" for ds in results["datasets"]
            ]
            out.append(f"| {lib['name']} | " + " | ".join(cells) + " |")
    out += [
        "",
        "## Excluded",
        "",
    ]
    excluded = [l for l in results["libraries"] if l.get("status") != "ok"]
    if excluded:
        for l in excluded:
            out.append(f"- **{l['name']}** — {l['status']}: {l.get('error', '')}")
    else:
        out.append("None — all entries ran and passed correctness.")
    return "\n".join(out) + "\n"


def inject(readme_text: str, table: str) -> str:
    if START not in readme_text or END not in readme_text:
        raise RuntimeError(f"README is missing {START} / {END} markers")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    return pattern.sub(f"{START}\n{table}\n{END}", readme_text)


def write_all(results: dict, readme: Path, results_md: Path) -> None:
    readme.write_text(inject(readme.read_text(encoding="utf-8"), render_table(results)), encoding="utf-8")
    results_md.write_text(render_results_md(results), encoding="utf-8")
