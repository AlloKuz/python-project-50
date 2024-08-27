from gendiff.formatters.stylish import prepare_value, format

import pytest
import json


@pytest.fixture
def file1_2_nested_diff():
    with open("tests/fixtures/file1_2_nested_diff.json") as f:
        data = json.load(f)
    return data


@pytest.fixture
def file1_2_nested_result():
    with open("tests/fixtures/file1_2_nested_result.json") as f:
        data = json.load(f)
    return data


@pytest.fixture
def file1_2_nested_str():
    with open("tests/fixtures/file1_2_nested_str.txt") as f:
        data = f.read()
    return data


@pytest.mark.parametrize("test_input,expected", [({"name": "value"}, "{"),
                                                 (True, "true"),
                                                 (False, "false"),
                                                 (None, "null"),
                                                 ({}, "{")])
def test_prepare_value(test_input, expected):
    assert prepare_value(test_input) == expected


def test_format(file1_2_nested_result, file1_2_nested_str):
    data = file1_2_nested_result
    result = file1_2_nested_str
    assert format(data) == result
