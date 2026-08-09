# Adding your library to the arena

A complete entry is a **two-file PR**. Maintainers of JSON libraries are explicitly welcome to submit their own.

## 1. Entry file — `entries/yourlib.toml`

```toml
name = "yourlib"                              # display name, unique
package = "yourlib"                           # pip install target (omit only for stdlib)
adapter = "jsonarena.adapters.yourlib_"       # module you add in step 2
repo = "https://github.com/you/yourlib"
language = "Rust"                             # hot-path implementation language
notes = "One line of context."                # optional
```

## 2. Adapter — `jsonarena/adapters/yourlib_.py`

```python
import yourlib

def loads(data: bytes):
    return yourlib.loads(data)

def dumps(obj):
    return yourlib.dumps(obj)   # str or bytes both fine

def version() -> str:
    return yourlib.__version__
```

## Rules

- **Defaults only.** The adapter must call your library the way your README tells users to. No undocumented fast paths, no disabling validation, no precomputed encoders beyond what your docs recommend as standard usage (a module-level reusable encoder object is fine if that's your documented idiom).
- **Correctness is a gate, not a metric.** Your library must parse identically to stdlib `json` (within 1e-9 float tolerance) and produce JSON that round-trips. Libraries failing the gate appear under the table as excluded, with the reason.
- **Wheels required.** CI installs with plain `pip install` on `ubuntu-latest` / CPython 3.12. If you need build flags, ship wheels first.
- **Scope:** general-purpose JSON parse/serialize for Python objects. Schema-first encoders may compete, but only through their untyped/dynamic API (the same one the correctness gate exercises).

## Check before you push

```bash
pip install -e . pytest yourlib
pytest -q                       # contract + correctness for every entry
jsonarena bench --quick
jsonarena render                # see where you land
```

Open the PR — CI reruns everything on neutral hardware and posts a leaderboard preview in the job summary. Numbers from your machine are ignored; the table is only ever written by CI on `main`.

## Disputes

If you think the harness undersells your library (dataset mix, missing op, unfair normalization), open an issue proposing a change to the *harness* — not a tuned adapter. Harness changes re-rank everyone and trigger a full leaderboard rebuild.
