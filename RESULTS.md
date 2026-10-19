# Full results

Python 3.12.15 · Linux x86_64 · 2026-10-19T10:27:37+00:00 · median of 10 runs

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
| msgspec | 7.01 | 5.58 | 2.99 | 88.57 |
| orjson | 6.02 | 5.35 | 4.07 | 90.57 |
| python-rapidjson | 9.57 | 9.04 | 7.24 | 127.99 |
| simplejson | 12.94 | 9.85 | 2.58 | 130.78 |
| json (stdlib) | 11.36 | 8.85 | 2.95 | 128.51 |
| ujson | 7.93 | 7.22 | 2.62 | 83.04 |

## Serialize (ms, lower is better)

| Library | numbers | structs | strings | mixed |
|---------|---:|---:|---:|---:|
| msgspec | 3.53 | 1.51 | 0.33 | 19.08 |
| orjson | 1.61 | 0.91 | 0.07 | 11.79 |
| python-rapidjson | 20.84 | 5.25 | 2.68 | 51.25 |
| simplejson | 39.56 | 17.75 | 1.27 | 207.27 |
| json (stdlib) | 22.65 | 9.18 | 2.05 | 74.97 |
| ujson | 7.67 | 5.54 | 3.36 | 45.11 |

## Excluded

None — all entries ran and passed correctness.
