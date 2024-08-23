from gendiff.utils.parse_file import parse_file
from gendiff.utils.cli import parse_args
from gendiff.utils.stringify import stringify


def main():
    args = parse_args()

    print(stringify(parse_file("example/file1.json")))


if __name__ == "__main__":
    main()
