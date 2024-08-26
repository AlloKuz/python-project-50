from .utils.make_json_diff import make_json_diff

import json


def format(data, raw=False):
    prepared_data = make_json_diff(data)
    return json.dumps(prepared_data)
