from gendiff.utils.parse_file import parse_file
from gendiff.utils.cli import parse_args
from gendiff.utils.stylish import stylish, stylish_plain
from gendiff.utils.make_diff import make_diff, format_diff


def generate_diff(file_path1, file_path2, format="json", formatter=None):
    file1_data = parse_file(file_path1)
    file2_data = parse_file(file_path2)
    if not formatter:
        if format == "json":
            formatter = stylish
        formatter = stylish_plain
    result = format_diff(make_diff(file1_data, file2_data), type=format)
    if formatter:
        result = formatter(result)

    return result


def main():
    args = parse_args()
    result = generate_diff(args.first_file,
                           args.second_file,
                           format=args.format)
    print(result)


if __name__ == "__main__":
    main()
