# Full results

Python 3.12.14 · Linux x86_64 · 2026-08-31T11:18:37+00:00 · median of 10 runs

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
| msgspec | 6.92 | 5.72 | 2.64 | 90.97 |
| orjson | 5.46 | 5.35 | 3.38 | 91.24 |
| python-rapidjson | 9.53 | 9.59 | 6.23 | 123.88 |
| simplejson | 12.85 | 10.50 | 2.20 | 136.02 |
| json (stdlib) | 11.34 | 9.62 | 2.49 | 139.65 |
| ujson | 7.62 | 7.49 | 2.14 | 96.85 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.54 | 1.60 | 0.29 | 16.65 |
| orjson | 2.01 | 1.23 | 0.10 | 13.69 |
| python-rapidjson | 23.47 | 5.79 | 2.73 | 53.32 |
| simplejson | 45.90 | 20.64 | 0.99 | 223.60 |
| json (stdlib) | 25.59 | 9.57 | 1.79 | 73.60 |
| ujson | 10.17 | 7.32 | 2.96 | 56.50 |

## Excluded

None — all entries ran and passed correctness.
