# Full results

Python 3.12.14 · Linux x86_64 · 2026-10-05T11:59:46+00:00 · median of 10 runs

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
| msgspec | 6.93 | 5.97 | 2.66 | 90.43 |
| orjson | 5.75 | 5.59 | 3.38 | 95.00 |
| python-rapidjson | 9.46 | 9.66 | 6.26 | 125.00 |
| simplejson | 12.92 | 10.53 | 2.19 | 128.65 |
| json (stdlib) | 11.43 | 9.75 | 2.48 | 120.89 |
| ujson | 7.55 | 7.31 | 2.26 | 89.82 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.55 | 1.60 | 0.30 | 16.86 |
| orjson | 2.01 | 1.21 | 0.10 | 14.06 |
| python-rapidjson | 23.91 | 5.76 | 2.77 | 54.20 |
| simplejson | 45.54 | 20.80 | 1.02 | 220.75 |
| json (stdlib) | 25.77 | 10.31 | 1.79 | 77.89 |
| ujson | 8.38 | 5.83 | 3.07 | 47.06 |

## Excluded

None — all entries ran and passed correctness.
