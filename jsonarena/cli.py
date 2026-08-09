"""jsonarena CLI: validate | deps | bench | render."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import leaderboard, runner
from .entry import EntryError, load_entries

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="jsonarena")
    p.add_argument("--entries", type=Path, default=ROOT / "entries")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validate", help="validate all entry TOML files")
    sub.add_parser("deps", help="print pip install targets for all entries")

    b = sub.add_parser("bench", help="run the benchmark")
    b.add_argument("--quick", action="store_true", help="3 repeats instead of 10")
    b.add_argument("--out", type=Path, default=ROOT / "results" / "results.json")

    r = sub.add_parser("render", help="rebuild README table + RESULTS.md from results JSON")
    r.add_argument("--results", type=Path, default=ROOT / "results" / "results.json")
    r.add_argument("--readme", type=Path, default=ROOT / "README.md")
    r.add_argument("--results-md", type=Path, default=ROOT / "RESULTS.md")

    args = p.parse_args(argv)

    try:
        entries = load_entries(args.entries)
    except EntryError as e:
        print(f"entry error: {e}", file=sys.stderr)
        return 1

    if args.cmd == "validate":
        print(f"OK: {len(entries)} entries valid")
        return 0

    if args.cmd == "deps":
        for e in entries:
            if e.package:
                print(e.package)
        return 0

    if args.cmd == "bench":
        repeats = 3 if args.quick else 10
        print(f"jsonarena: {len(entries)} entries, {repeats} repeats", file=sys.stderr)
        results = runner.run(entries, repeats=repeats)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
        ok = [l for l in results["libraries"] if l["status"] == "ok"]
        return 0 if ok else 1

    if args.cmd == "render":
        results = json.loads(args.results.read_text(encoding="utf-8"))
        leaderboard.write_all(results, args.readme, args.results_md)
        print(f"rebuilt {args.readme} and {args.results_md}", file=sys.stderr)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
