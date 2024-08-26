from gendiff.formatters.stylish import is_dict, prepare_value, format

import pytest
import json


@pytest.fixture
def nested_data_expected_dict():
    with open("tests/fixtures/nested_data_expected_dict.json") as f:
        data = json.load(f)
    return data


@pytest.fixture
def nested_data_expected_diff():
    with open("tests/fixtures/nested_data_expected_diff.json") as f:
        data = json.load(f)
    return data


def test_is_dict():
    assert is_dict({})
    assert is_dict({"a": "b"})
    assert not is_dict([])


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


def test_format(nested_data_expected_diff, nested_data_expected_dict):
    value = nested_data_expected_diff
    expected = nested_data_expected_dict
    raw = True
    assert format(value, raw=raw) == expected
