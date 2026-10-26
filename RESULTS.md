# Full results

Python 3.12.15 · Linux x86_64 · 2026-10-26T10:43:10+00:00 · median of 10 runs

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
| msgspec | 5.91 | 4.63 | 2.25 | 91.31 |
| orjson | 4.56 | 4.34 | 2.94 | 98.60 |
| python-rapidjson | 7.43 | 7.28 | 5.48 | 133.67 |
| simplejson | 9.66 | 8.35 | 1.95 | 145.89 |
| json (stdlib) | 8.75 | 7.77 | 2.02 | 150.97 |
| ujson | 6.19 | 6.23 | 2.05 | 91.42 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 2.96 | 1.26 | 0.21 | 15.35 |
| orjson | 1.53 | 0.80 | 0.06 | 10.29 |
| python-rapidjson | 17.88 | 4.38 | 2.12 | 41.84 |
| simplejson | 34.37 | 15.96 | 0.84 | 201.26 |
| json (stdlib) | 18.99 | 7.52 | 1.63 | 59.08 |
| ujson | 6.59 | 4.31 | 2.56 | 35.87 |

## Excluded

None — all entries ran and passed correctness.
