from gendiff.formatters.stylish import prepare_value

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


def test_prepare_value():
    value = {"name": "value"}
    expected = "{"
    assert prepare_value(value) == expected

    value = True
    expected = "true"
    assert prepare_value(value) == expected

    value = False
    expected = "false"
    assert prepare_value(value) == expected

    value = None
    expected = "null"
    assert prepare_value(value) == expected

    value = "https"
    expected = "https"
    assert prepare_value(value) == expected

    value = {}
    expected = "{"
    assert prepare_value(value) == expected
