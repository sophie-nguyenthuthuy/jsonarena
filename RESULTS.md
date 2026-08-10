# Full results

Python 3.12.13 · Linux x86_64 · 2026-08-10T06:08:23+00:00 · median of 10 runs

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
| msgspec | 6.57 | 5.71 | 2.63 | 98.66 |
| orjson | 5.49 | 5.50 | 3.41 | 97.02 |
| python-rapidjson | 9.47 | 9.75 | 6.26 | 135.50 |
| simplejson | 12.23 | 10.97 | 2.21 | 143.66 |
| json (stdlib) | 11.26 | 9.61 | 2.49 | 134.87 |
| ujson | 7.64 | 7.68 | 2.13 | 97.75 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.53 | 1.59 | 0.30 | 16.73 |
| orjson | 2.22 | 1.09 | 0.11 | 13.10 |
| python-rapidjson | 23.74 | 5.82 | 2.72 | 53.72 |
| simplejson | 45.77 | 20.59 | 0.97 | 219.32 |
| json (stdlib) | 25.64 | 10.03 | 1.76 | 75.83 |
| ujson | 10.08 | 7.00 | 3.09 | 53.79 |

## Excluded

None — all entries ran and passed correctness.
