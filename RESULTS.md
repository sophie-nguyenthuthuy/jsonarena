# Full results

Python 3.12.15 · Linux x86_64 · 2026-11-02T13:01:47+00:00 · median of 10 runs

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
| msgspec | 4.88 | 3.63 | 2.08 | 72.48 |
| orjson | 3.77 | 3.24 | 2.86 | 87.69 |
| python-rapidjson | 5.85 | 5.70 | 5.20 | 119.10 |
| simplejson | 7.37 | 6.38 | 1.78 | 122.32 |
| json (stdlib) | 6.70 | 5.96 | 1.88 | 125.15 |
| ujson | 4.66 | 4.36 | 1.97 | 78.01 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 2.45 | 0.95 | 0.15 | 12.85 |
| orjson | 1.07 | 0.49 | 0.03 | 8.59 |
| python-rapidjson | 13.09 | 3.11 | 1.90 | 33.77 |
| simplejson | 26.61 | 11.96 | 0.66 | 140.95 |
| json (stdlib) | 14.45 | 5.25 | 1.34 | 43.99 |
| ujson | 5.44 | 3.31 | 2.30 | 31.14 |

## Excluded

None — all entries ran and passed correctness.
