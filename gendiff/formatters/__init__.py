from .json import format as json_formatter
from .plain import format as plain_formatter
from .stylish import format as stylish_formatter


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


__all__ = (
    "json_formatter",
    "plain_formatter",
    "stylish_formatter",
    "format_data",
)
