# jsonarena 🏟️

**Community benchmark arena for Python JSON libraries.** PR your library as one TOML file + one tiny adapter — CI runs the benchmark, verifies correctness, and rebuilds this leaderboard automatically. No human edits the table.

## Leaderboard

<!-- LEADERBOARD:START -->
| Rank | Library | Version | Lang | Parse | Serialize | Overall |
|-----:|---------|---------|------|------:|----------:|--------:|
| 🥇 | [orjson](https://github.com/ijl/orjson) | 3.11.9 | Rust | 1.35× | 9.58× | **3.60×** |
| 🥈 | [msgspec](https://github.com/jcrist/msgspec) | 0.21.1 | C | 1.36× | 5.89× | **2.83×** |
| 🥉 | [ujson](https://github.com/ultrajson/ultrajson) | 5.13.0 | C | 1.32× | 1.29× | **1.30×** |
| 4 | [json (stdlib)](https://github.com/python/cpython) | py3.12 | C | 1.00× | 1.00× | **1.00×** |
| 5 | [python-rapidjson](https://github.com/python-rapidjson/python-rapidjson) | 1.23 | C++ | 0.81× | 1.12× | **0.95×** |
| 6 | [simplejson](https://github.com/simplejson/simplejson) | 4.1.1 | C | 0.96× | 0.63× | **0.78×** |

*Speed relative to the stdlib baseline (higher is better), geometric mean over 4 datasets. Python 3.12.13, Linux x86_64, 2026-08-09T02:49:02+00:00. Full numbers in [RESULTS.md](RESULTS.md).*
<!-- LEADERBOARD:END -->

## How it works

1. **Entries are data.** Each library is one file in [`entries/`](entries/) plus a ~15-line adapter in [`jsonarena/adapters/`](jsonarena/adapters/) exposing `loads(bytes)`, `dumps(obj)`, `version()`. Defaults only — no hand-tuned flags.
2. **Correctness gates speed.** Before timing, every library must round-trip four datasets against the stdlib parse (`deep_eq` with float tolerance, strict on bool/int confusion). Fail the gate → excluded from the table, publicly, with the reason.
3. **Datasets are seeded, not vendored.** Four ~1 MB payloads (float-heavy, record array, Vietnamese unicode text, nested mixed tree) are regenerated deterministically from a fixed seed at bench time — no fixture files, no cherry-picking.
4. **CI owns the table.** Every merge to `main` (and a weekly cron, to catch upstream releases) reruns the full bench on GitHub Actions hardware and commits the README table + [RESULTS.md](RESULTS.md) back. PRs get a preview table in the job summary.

Scores are relative throughput vs the stdlib baseline (geometric mean across datasets; serialize throughput is normalized by canonical payload size so compact output isn't penalized).

## Add your library

See [CONTRIBUTING.md](CONTRIBUTING.md) — it's a two-file PR:

```bash
git clone https://github.com/sophie-nguyenthuthuy/jsonarena && cd jsonarena
pip install -e . pytest
# add entries/yourlib.toml + jsonarena/adapters/yourlib_.py
pip install yourlib && pytest -q && jsonarena bench --quick && jsonarena render
```

## Run locally

```bash
pip install -e .
pip install $(jsonarena deps)   # all entry packages
jsonarena bench                  # writes results/results.json
jsonarena render                 # rebuilds README table + RESULTS.md
```

## Caveats

- Single-machine, single-process wall-clock medians. Rankings on your hardware/payloads may differ — that's why the datasets and runner are 200 lines you can read.
- Measures the *default* configuration of each library, deliberately.

MIT.
