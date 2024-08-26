from gendiff.parse_file import parse_file
from gendiff.formatters import (stylish_formatter,
                                plain_formatter,
                                json_formatter)
from gendiff.make_diff import make_diff


def generate_diff(file_path1,
                  file_path2,
                  output_type=None,
                  formatter=None):
    file1_data = parse_file(file_path1)
    file2_data = parse_file(file_path2)

    if not formatter:
        match output_type:
            case "json":
                formatter = json_formatter
            case "plain":
                formatter = plain_formatter
            case _:
                formatter = stylish_formatter

    result = formatter(make_diff(file1_data, file2_data))

    return result
