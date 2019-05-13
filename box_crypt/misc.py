import json
import base64


def encode(b):
    return base64.b64encode(b)


def decode(str):
    return base64.b64decode(str)


def dict_to_json(obj):
    return json.dumps(obj, separators=(',', ':'))


def json_to_dict(data):
    return json.loads(data)
