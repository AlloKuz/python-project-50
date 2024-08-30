import argparse


def parse_args():
    """
    Creates an argument parser instance with options
    for two files and an output format.
    """
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format",
                        metavar="FORMAT",
                        type=str,
                        choices=["plain", "json", "stylish"],
                        default="stylish",
                        help="set format of output")

    return parser.parse_args()
