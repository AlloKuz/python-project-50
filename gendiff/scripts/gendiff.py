from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    """
    Returns the difference between two files in the specified format
    according to the arguments passed.
    """
    args = parse_args()

    result = generate_diff(args.first_file,
                           args.second_file,
                           output_type=args.format)

    print(result)


if __name__ == "__main__":
    main()
