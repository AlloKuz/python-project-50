from .utils.make_json_diff import make_json_diff
from .stylish import _format_stylish

import json


def format(data, raw=False):
    prepared_data = make_json_diff(data)
    return prepared_data if not raw else json.dumps(prepared_data)
