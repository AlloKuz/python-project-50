from gendiff.parse import parse_by_filename
from gendiff.make_diff import make_diff
from gendiff.formatters import format_data


def generate_diff(file_path1,
                  file_path2,
                  output_type=None,
                  formatter=None):

    file1_data = parse_by_filename(file_path1)
    file2_data = parse_by_filename(file_path2)

    result = format_data(make_diff(file1_data, file2_data),
                         output_type,
                         formatter)
    return result
