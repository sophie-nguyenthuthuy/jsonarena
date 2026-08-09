import orjson


def loads(data: bytes):
    return orjson.loads(data)


def dumps(obj):
    return orjson.dumps(obj)


def version() -> str:
    return orjson.__version__
