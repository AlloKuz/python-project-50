from .utils.make_json_diff import make_json_diff

import json


def format(data):
    return json.dumps(make_json_diff(data))
