# Full results

Python 3.12.15 · Linux x86_64 · 2026-10-12T12:40:57+00:00 · median of 10 runs

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
| msgspec | 4.56 | 3.69 | 2.07 | 83.56 |
| orjson | 3.50 | 3.44 | 2.87 | 88.73 |
| python-rapidjson | 5.86 | 5.51 | 5.37 | 118.68 |
| simplejson | 7.62 | 6.24 | 1.82 | 127.70 |
| json (stdlib) | 6.64 | 5.38 | 1.99 | 112.88 |
| ujson | 4.90 | 4.78 | 2.02 | 89.41 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 2.58 | 1.00 | 0.16 | 13.84 |
| orjson | 1.14 | 0.52 | 0.03 | 8.99 |
| python-rapidjson | 14.35 | 3.22 | 1.96 | 35.58 |
| simplejson | 27.46 | 12.43 | 0.68 | 153.60 |
| json (stdlib) | 14.56 | 5.32 | 1.30 | 46.15 |
| ujson | 5.31 | 3.39 | 2.36 | 33.71 |

## Excluded

None — all entries ran and passed correctness.
