# Full results

Python 3.12.14 · Linux x86_64 · 2026-09-07T09:54:36+00:00 · median of 10 runs

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
| msgspec | 6.98 | 5.66 | 2.61 | 89.88 |
| orjson | 5.69 | 5.32 | 3.37 | 92.36 |
| python-rapidjson | 9.47 | 9.38 | 6.22 | 131.83 |
| simplejson | 12.76 | 10.40 | 2.19 | 132.28 |
| json (stdlib) | 11.19 | 9.41 | 2.48 | 127.37 |
| ujson | 7.55 | 7.23 | 2.28 | 85.27 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.52 | 1.58 | 0.29 | 16.19 |
| orjson | 2.09 | 1.24 | 0.10 | 13.72 |
| python-rapidjson | 23.68 | 5.72 | 2.76 | 53.46 |
| simplejson | 45.49 | 20.43 | 0.98 | 217.00 |
| json (stdlib) | 25.46 | 9.60 | 1.78 | 73.22 |
| ujson | 8.36 | 5.51 | 2.78 | 46.89 |

## Excluded

None — all entries ran and passed correctness.
