from gendiff.parser import get_content
from gendiff.diff_maker import make_diff
from gendiff.formatters.__init__ import format_data


def generate_diff(file_path1,
                  file_path2,
                  output_type=None):

    """
    Calculates the difference between files, formats it
    and returns the result.
    """
    content1 = get_content(file_path1)
    content2 = get_content(file_path2)

    result = format_data(make_diff(content1, content2),
                         output_type)
    return result
