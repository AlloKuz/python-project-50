from . import stylish

import json


def format(data):
    return json.dumps(stylish.make_json_diff(data))
