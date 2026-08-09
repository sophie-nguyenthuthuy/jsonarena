"""Baseline: the standard library."""
import json
import sys


def loads(data: bytes):
    return json.loads(data)


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def version() -> str:
    return f"py{sys.version_info.major}.{sys.version_info.minor}"
