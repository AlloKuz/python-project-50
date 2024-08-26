from gendiff.parser import get_content
from gendiff.diff_maker import make_diff
from gendiff.formatters import format_data


def generate_diff(file_path1,
                  file_path2,
                  output_type=None,
                  formatter=None):

    file1_data = get_content(file_path1)
    file2_data = get_content(file_path2)

    result = format_data(make_diff(file1_data, file2_data),
                         output_type,
                         formatter)
    return result
