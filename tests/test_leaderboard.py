import pytest

from jsonarena.leaderboard import END, START, inject, rank, render_results_md, render_table

RESULTS = {
    "meta": {
        "timestamp": "2026-08-09T00:00:00+00:00",
        "python": "3.12.0",
        "platform": "Linux x86_64",
        "repeats": 10,
    },
    "datasets": {"a": {"bytes": 1_000_000}, "b": {"bytes": 2_000_000}},
    "libraries": [
        {
            "name": "base",
            "repo": "https://x/base",
            "language": "C",
            "baseline": True,
            "status": "ok",
            "version": "1.0",
            "benchmarks": {
                "a": {"parse_s": 0.010, "serialize_s": 0.010},
                "b": {"parse_s": 0.020, "serialize_s": 0.020},
            },
        },
        {
            "name": "fast",
            "repo": "https://x/fast",
            "language": "Rust",
            "baseline": False,
            "status": "ok",
            "version": "2.0",
            "benchmarks": {
                "a": {"parse_s": 0.002, "serialize_s": 0.005},
                "b": {"parse_s": 0.004, "serialize_s": 0.010},
            },
        },
        {
            "name": "broken",
            "repo": "https://x/broken",
            "baseline": False,
            "status": "failed-correctness",
            "error": "loads output differs",
        },
    ],
}


def test_rank_orders_fastest_first_and_scores_relative():
    rows = rank(RESULTS)
    assert [r["name"] for r in rows] == ["fast", "base"]
    assert rows[1]["overall_x"] == pytest.approx(1.0)
    assert rows[0]["parse_x"] == pytest.approx(5.0)
    assert rows[0]["serialize_x"] == pytest.approx(2.0)
    assert rows[0]["overall_x"] == pytest.approx(10 ** 0.5, rel=1e-6)


def test_render_table_includes_medals_and_exclusions():
    table = render_table(RESULTS)
    assert "🥇" in table and "[fast](https://x/fast)" in table
    assert "broken" in table and "failed-correctness" in table


def test_missing_baseline_raises():
    bad = {**RESULTS, "libraries": [l for l in RESULTS["libraries"] if not l.get("baseline")]}
    with pytest.raises(RuntimeError, match="baseline"):
        rank(bad)


def test_inject_replaces_only_marker_region():
    readme = f"# Title\n\n{START}\nold\n{END}\n\nfooter"
    out = inject(readme, "NEW TABLE")
    assert "NEW TABLE" in out and "old" not in out
    assert out.startswith("# Title") and out.endswith("footer")
    # idempotent on re-render
    assert inject(out, "NEW TABLE") == out


def test_inject_requires_markers():
    with pytest.raises(RuntimeError, match="markers"):
        inject("no markers here", "x")


def test_results_md_renders():
    md = render_results_md(RESULTS)
    assert "## Parse" in md and "## Serialize" in md and "broken" in md
