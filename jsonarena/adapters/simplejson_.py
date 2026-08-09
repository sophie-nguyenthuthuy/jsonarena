import simplejson


def loads(data: bytes):
    return simplejson.loads(data)


def dumps(obj):
    return simplejson.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def version() -> str:
    return simplejson.__version__
