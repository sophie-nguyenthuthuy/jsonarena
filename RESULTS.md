# Full results

Python 3.12.16 · Linux x86_64 · 2026-11-16T13:18:43+00:00 · median of 10 runs

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
| msgspec | 5.24 | 4.47 | 2.24 | 63.24 |
| orjson | 4.45 | 4.40 | 3.12 | 69.66 |
| python-rapidjson | 7.24 | 7.20 | 5.51 | 97.75 |
| simplejson | 9.43 | 7.77 | 1.96 | 97.88 |
| json (stdlib) | 8.79 | 7.14 | 2.01 | 93.91 |
| ujson | 6.15 | 6.03 | 2.04 | 62.28 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 2.79 | 1.19 | 0.24 | 14.05 |
| orjson | 1.25 | 0.71 | 0.06 | 8.81 |
| python-rapidjson | 15.36 | 3.92 | 2.04 | 37.88 |
| simplejson | 28.58 | 13.28 | 0.78 | 144.35 |
| json (stdlib) | 16.91 | 7.03 | 1.61 | 54.88 |
| ujson | 5.87 | 4.27 | 2.61 | 34.63 |

## Excluded

None — all entries ran and passed correctness.
