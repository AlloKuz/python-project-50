from gendiff.formatters import (json_formatter,
                                plain_formatter,
                                stylish_formatter)
from .utils.make_json_diff import make_json_diff


def format_data(data, output_type="json", formatter=None):
    if not formatter:
        match output_type:
            case "json":
                formatter = json_formatter
            case "plain":
                formatter = plain_formatter
            case _:
                formatter = stylish_formatter
    if output_type == "plain":
        return formatter(data)
    return formatter(make_json_diff(data))
