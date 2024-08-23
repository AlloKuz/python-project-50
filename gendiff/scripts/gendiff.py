import argparse


def main():
    parser = argparse.ArgumentParser(
                prog="gendiff",
                description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    args = parser.parse_args()


if __name__ == "__main__":
    main()
