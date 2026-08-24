# Full results

Python 3.12.14 · Linux x86_64 · 2026-08-24T05:33:46+00:00 · median of 10 runs

## Datasets

| Dataset | Size |
|---------|-----:|
| numbers | 0.79 MB |
| structs | 0.73 MB |
| strings | 0.61 MB |
| mixed | 4.58 MB |

## Parse (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 7.62 | 6.03 | 2.90 | 102.13 |
| orjson | 5.88 | 5.58 | 3.86 | 107.12 |
| python-rapidjson | 9.56 | 9.49 | 7.12 | 147.13 |
| simplejson | 12.30 | 10.32 | 2.47 | 153.99 |
| json (stdlib) | 10.86 | 9.34 | 2.76 | 147.74 |
| ujson | 8.07 | 7.50 | 2.52 | 103.06 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.85 | 1.62 | 0.31 | 19.13 |
| orjson | 2.00 | 1.28 | 0.09 | 16.03 |
| python-rapidjson | 23.57 | 5.72 | 2.65 | 54.12 |
| simplejson | 44.70 | 20.25 | 1.06 | 228.72 |
| json (stdlib) | 24.66 | 9.54 | 2.07 | 75.36 |
| ujson | 10.49 | 7.13 | 3.22 | 54.74 |

## Excluded

None — all entries ran and passed correctness.
