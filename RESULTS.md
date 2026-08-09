# Full results

Python 3.12.13 · Linux x86_64 · 2026-08-09T02:49:02+00:00 · median of 10 runs

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
| msgspec | 7.03 | 5.78 | 2.65 | 96.82 |
| orjson | 5.54 | 5.63 | 3.43 | 101.78 |
| python-rapidjson | 9.55 | 9.60 | 6.33 | 146.00 |
| simplejson | 12.26 | 10.77 | 2.22 | 144.82 |
| json (stdlib) | 11.35 | 9.52 | 2.51 | 133.51 |
| ujson | 7.63 | 7.51 | 2.13 | 97.68 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.53 | 1.60 | 0.30 | 16.64 |
| orjson | 2.22 | 1.10 | 0.12 | 13.38 |
| python-rapidjson | 24.16 | 5.81 | 2.80 | 54.10 |
| simplejson | 46.29 | 20.69 | 0.98 | 219.44 |
| json (stdlib) | 25.75 | 9.68 | 1.77 | 75.35 |
| ujson | 9.88 | 7.17 | 3.08 | 55.51 |

## Excluded

None — all entries ran and passed correctness.
