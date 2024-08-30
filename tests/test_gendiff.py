from gendiff import generate_diff
from parser import parse
from gendiff.formatters.plain import transform_to_str

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


def test_exception_type_of_file():
    assert parse(
        'tests/fixtures/json_difference_for_test_data.txt'
    ) == {'Exception': 'file has wrong format'}


def test_exception_format():
    for value in ['50', [True], 'text',]:
        assert transform_to_str(value) == f"'{str(value)}'"
    assert transform_to_str(True) == 'true'
    assert transform_to_str(False) == 'false'
    assert transform_to_str(None) == 'null'
    assert transform_to_str(50) == 50
    assert transform_to_str('[complex value]') == '[complex value]'
