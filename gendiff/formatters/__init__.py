from gendiff.formatters.json import json_formatter
from gendiff.formatters.plain import plain_formatter,
from gendiff.formatters.stylish import stylish_formatter


def format_data(data, output_type="json"):
    """
    Formats data according to the selected formatting type.
    """
    match output_type:
        case "json":
            return json_formatter(data)
        case "plain":
            return plain_formatter(data)
        case _:
            return stylish_formatter(data)
