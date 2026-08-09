import rapidjson


def loads(data: bytes):
    return rapidjson.loads(data)


def dumps(obj):
    return rapidjson.dumps(obj, ensure_ascii=False)


def version() -> str:
    return rapidjson.__version__
