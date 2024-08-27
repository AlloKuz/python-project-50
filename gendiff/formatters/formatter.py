from gendiff.formatters import (json_formatter,
                                plain_formatter,
                                stylish_formatter)


def format_data(data, output_type="json"):
    match output_type:
        case "json":
            return json_formatter(data)
        case "plain":
            return plain_formatter(data)
        case _:
            return stylish_formatter(data)
