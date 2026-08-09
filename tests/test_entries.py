import pytest

from jsonarena.entry import EntryError, load_entries, load_entry
from jsonarena.cli import ROOT


def test_repo_entries_are_valid():
    entries = load_entries(ROOT / "entries")
    assert len(entries) >= 2
    assert sum(e.baseline for e in entries) == 1


def test_missing_field_rejected(tmp_path):
    (tmp_path / "bad.toml").write_text('name = "x"\n')
    with pytest.raises(EntryError, match="missing required"):
        load_entry(tmp_path / "bad.toml")


def test_unknown_field_rejected(tmp_path):
    (tmp_path / "bad.toml").write_text(
        'name = "x"\nadapter = "a.b"\nrepo = "https://x"\nspeed_hack = true\n'
    )
    with pytest.raises(EntryError, match="unknown field"):
        load_entry(tmp_path / "bad.toml")


def test_duplicate_names_rejected(tmp_path):
    for fn in ("a.toml", "b.toml"):
        (tmp_path / fn).write_text(
            'name = "x"\nadapter = "a.b"\nrepo = "https://x"\nbaseline = true\n'
        )
    with pytest.raises(EntryError, match="duplicate"):
        load_entries(tmp_path)


def test_exactly_one_baseline_required(tmp_path):
    (tmp_path / "a.toml").write_text('name = "x"\nadapter = "a.b"\nrepo = "https://x"\n')
    with pytest.raises(EntryError, match="baseline"):
        load_entries(tmp_path)


def test_non_https_repo_rejected(tmp_path):
    (tmp_path / "a.toml").write_text('name = "x"\nadapter = "a.b"\nrepo = "http://x"\n')
    with pytest.raises(EntryError, match="https"):
        load_entry(tmp_path / "a.toml")
