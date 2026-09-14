# Full results

Python 3.12.14 · Linux x86_64 · 2026-09-14T10:16:34+00:00 · median of 10 runs

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
| msgspec | 6.54 | 5.72 | 2.62 | 89.98 |
| orjson | 5.42 | 5.48 | 3.38 | 94.27 |
| python-rapidjson | 9.44 | 9.54 | 6.28 | 134.29 |
| simplejson | 12.77 | 10.56 | 2.19 | 137.16 |
| json (stdlib) | 11.35 | 9.67 | 2.48 | 128.39 |
| ujson | 7.57 | 7.29 | 2.26 | 93.24 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.50 | 1.58 | 0.30 | 16.38 |
| orjson | 2.00 | 1.25 | 0.10 | 13.93 |
| python-rapidjson | 24.81 | 5.73 | 2.80 | 52.89 |
| simplejson | 45.66 | 20.45 | 0.98 | 220.49 |
| json (stdlib) | 26.23 | 9.80 | 1.81 | 73.61 |
| ujson | 8.53 | 5.46 | 2.76 | 47.08 |

## Excluded

None — all entries ran and passed correctness.
