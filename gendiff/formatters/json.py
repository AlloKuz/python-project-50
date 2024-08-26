from .utils.make_json_diff import make_json_diff
from .stylish import _format_stylish


def format(data, raw=False):
    prepared_data = make_json_diff(data)
    return prepared_data if not raw else _format_stylish(prepared_data,
                                                     indent_symbol="",
                                                     indent_size=0,
                                                     shift_size=0)
