from gendiff.formatters import (json_formatter,
                                plain_formatter,
                                stylish_formatter)
from .utils.make_json_diff import make_json_diff


def format_data(data, output_type="json", formatter=None):
    if formatter:
        return formatter(data)
    match output_type:
        case "json":
            return json_formatter(make_json_diff(data))
        case "plain":
            return plain_formatter(data)
        case _:
            return stylish_formatter(make_json_diff(data))
