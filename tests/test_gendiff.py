from gendiff import generate_diff

import pytest

FIXTURES_PATH = "tests/fixtures"


@pytest.mark.parametrize("file1, file2, expected_path, output_type", [
    (
        f"{FIXTURES_PATH}/file1_nested.yaml",
        f"{FIXTURES_PATH}/file2_nested.yaml",
        f"{FIXTURES_PATH}/file1_2_plain.txt",
        "plain"
    ),
    (
        f"{FIXTURES_PATH}/file1_nested.json",
        f"{FIXTURES_PATH}/file2_nested.yaml",
        f"{FIXTURES_PATH}/file1_2_json.txt",
        "json"
    ),
    (
        f"{FIXTURES_PATH}/file1_nested.yaml",
        f"{FIXTURES_PATH}/file2_nested.yaml",
        f"{FIXTURES_PATH}/file1_2_stylish.txt",
        "stylish"
    ),

])
def test_gen_diff_output(file1, file2, expected_path, output_type):
    with open(expected_path) as f:
        assert generate_diff(file1, file2, output_type=output_type) == f.read()
