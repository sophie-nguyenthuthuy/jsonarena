# Full results

Python 3.13.9 · Darwin arm64 · 2026-08-09T02:47:16+00:00 · median of 10 runs

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
| msgspec | 4.24 | 3.51 | 1.83 | 51.68 |
| orjson | 3.97 | 3.26 | 2.84 | 56.76 |
| python-rapidjson | 6.09 | 6.32 | 5.18 | 81.94 |
| simplejson | 8.37 | 6.96 | 2.04 | 102.32 |
| json (stdlib) | 6.62 | 5.72 | 2.24 | 87.99 |
| ujson | 5.64 | 4.69 | 1.75 | 53.69 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 2.54 | 1.05 | 0.23 | 13.56 |
| orjson | 1.33 | 0.83 | 0.11 | 9.47 |
| python-rapidjson | 13.75 | 3.44 | 2.73 | 31.93 |
| simplejson | 22.69 | 10.79 | 0.92 | 130.80 |
| json (stdlib) | 15.05 | 6.20 | 1.33 | 48.72 |
| ujson | 6.77 | 4.71 | 2.49 | 36.39 |

## Excluded

None — all entries ran and passed correctness.
