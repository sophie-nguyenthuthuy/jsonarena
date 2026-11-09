# Full results

Python 3.12.16 · Linux x86_64 · 2026-11-09T13:33:36+00:00 · median of 10 runs

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
| msgspec | 5.89 | 4.66 | 2.25 | 76.72 |
| orjson | 4.84 | 4.30 | 2.94 | 90.18 |
| python-rapidjson | 7.45 | 7.22 | 5.45 | 113.78 |
| simplejson | 9.39 | 7.88 | 1.92 | 117.09 |
| json (stdlib) | 8.50 | 7.37 | 2.01 | 115.20 |
| ujson | 6.14 | 5.88 | 2.02 | 76.39 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 2.95 | 1.26 | 0.24 | 14.59 |
| orjson | 1.52 | 0.80 | 0.06 | 9.94 |
| python-rapidjson | 17.63 | 4.36 | 2.11 | 42.08 |
| simplejson | 33.55 | 15.55 | 0.83 | 171.72 |
| json (stdlib) | 18.67 | 7.42 | 1.63 | 56.91 |
| ujson | 6.30 | 4.31 | 2.54 | 36.36 |

## Excluded

None — all entries ran and passed correctness.
