# Full results

Python 3.12.14 · Linux x86_64 · 2026-09-28T11:23:58+00:00 · median of 10 runs

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
| msgspec | 7.19 | 5.83 | 2.65 | 91.09 |
| orjson | 5.69 | 5.37 | 3.37 | 96.61 |
| python-rapidjson | 9.54 | 9.41 | 6.29 | 142.98 |
| simplejson | 13.14 | 10.71 | 2.20 | 144.31 |
| json (stdlib) | 11.31 | 9.47 | 2.48 | 138.40 |
| ujson | 7.66 | 7.32 | 2.29 | 93.34 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.52 | 1.61 | 0.30 | 16.58 |
| orjson | 2.02 | 1.24 | 0.10 | 14.04 |
| python-rapidjson | 24.07 | 5.77 | 2.79 | 54.25 |
| simplejson | 48.02 | 21.08 | 0.98 | 225.89 |
| json (stdlib) | 25.75 | 9.93 | 1.78 | 75.88 |
| ujson | 8.40 | 5.49 | 3.08 | 44.85 |

## Excluded

None — all entries ran and passed correctness.
