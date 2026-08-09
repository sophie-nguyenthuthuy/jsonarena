import msgspec
import msgspec.json

_decoder = msgspec.json.Decoder()
_encoder = msgspec.json.Encoder()


def loads(data: bytes):
    return _decoder.decode(data)


def dumps(obj):
    return _encoder.encode(obj)


def version() -> str:
    return msgspec.__version__
