# Full results

Python 3.12.14 · Linux x86_64 · 2026-09-21T10:21:54+00:00 · median of 10 runs

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
| msgspec | 6.98 | 5.74 | 2.61 | 90.83 |
| orjson | 5.48 | 5.43 | 3.37 | 95.28 |
| python-rapidjson | 9.47 | 9.51 | 6.27 | 140.09 |
| simplejson | 12.80 | 10.89 | 2.20 | 131.37 |
| json (stdlib) | 11.16 | 9.78 | 2.47 | 134.15 |
| ujson | 7.53 | 7.15 | 2.28 | 89.57 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.52 | 1.60 | 0.30 | 16.36 |
| orjson | 2.00 | 1.24 | 0.10 | 13.78 |
| python-rapidjson | 23.73 | 5.71 | 2.76 | 53.97 |
| simplejson | 46.49 | 20.69 | 0.98 | 217.71 |
| json (stdlib) | 25.45 | 9.78 | 1.78 | 73.74 |
| ujson | 8.59 | 5.61 | 3.06 | 46.30 |

## Excluded

None — all entries ran and passed correctness.
