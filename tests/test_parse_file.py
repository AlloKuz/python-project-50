from gendiff.parser import get_content

import pytest


def test_parse_file():
    filepath_json = "tests/fixtures/make_diff_data_1.json"
    expected = {"host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False}
    assert get_content(filepath_json) == expected

    filepath_yaml = "tests/fixtures/make_diff_data_1.yaml"
    assert get_content(filepath_yaml) == expected

    with pytest.raises(ValueError):
        get_content("java.txt")
