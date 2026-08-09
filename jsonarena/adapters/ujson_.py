import ujson


def loads(data: bytes):
    return ujson.loads(data)


def dumps(obj):
    return ujson.dumps(obj, ensure_ascii=False)


def version() -> str:
    return ujson.__version__
