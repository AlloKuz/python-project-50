from gendiff.utils.parse_file import parse_file
from gendiff.utils.cli import parse_args
from gendiff.utils.stringify import stringify
from gendiff.utils.make_diff import make_and_format_diff


def generate_diff(file_path1, file_path2):
    file1_data = parse_file(file_path1)
    file2_data = parse_file(file_path2)
    result = make_and_format_diff(file1_data, file2_data)
    return stringify(result)


def main():
    args = parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()
