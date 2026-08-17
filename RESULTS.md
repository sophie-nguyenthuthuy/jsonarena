# Full results

Python 3.12.13 · Linux x86_64 · 2026-08-17T05:30:55+00:00 · median of 10 runs

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
| msgspec | 6.91 | 5.60 | 2.67 | 84.14 |
| orjson | 5.52 | 5.44 | 3.37 | 90.19 |
| python-rapidjson | 9.42 | 9.67 | 6.30 | 122.10 |
| simplejson | 12.34 | 10.85 | 2.21 | 125.49 |
| json (stdlib) | 11.37 | 9.45 | 2.49 | 120.34 |
| ujson | 7.49 | 7.46 | 2.14 | 85.55 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.50 | 1.59 | 0.29 | 16.31 |
| orjson | 1.99 | 1.26 | 0.10 | 13.62 |
| python-rapidjson | 23.61 | 5.91 | 2.79 | 52.92 |
| simplejson | 44.58 | 19.99 | 0.98 | 207.69 |
| json (stdlib) | 25.27 | 9.72 | 1.77 | 73.93 |
| ujson | 10.01 | 7.02 | 3.07 | 54.32 |

## Excluded

None — all entries ran and passed correctness.
