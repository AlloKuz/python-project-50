from gendiff.parse import parse_by_filename

import pytest


def test_parse_file():
    filepath_json = "tests/fixtures/make_diff_data_1.json"
    expected = {"host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False}
    assert parse_by_filename(filepath_json) == expected

    filepath_yaml = "tests/fixtures/make_diff_data_1.yaml"
    assert parse_by_filename(filepath_yaml) == expected

    with pytest.raises(ValueError):
        parse_by_filename("java.txt")
