from gendiff.formatters.plain import transform_to_str, format

import pytest
import json


def test_transform_to_str():
    data = {"value": 1}
    result = transform_to_str(data)
    assert result == "[complex value]"

    data = True
    result = transform_to_str(data)
    assert result == "true"

    data = None
    result = transform_to_str(data)
    assert result == "null"

    data = "value"
    result = transform_to_str(data)
    assert result == "'value'"

    data = 1
    result = transform_to_str(data)
    assert result == 1


@pytest.fixture
def file1_2_nested_plain():
    with open("tests/fixtures/file1_2_nested_plain.txt") as f:
        data = f.read()
    return data


@pytest.fixture
def file1_2_nested_diff():
    with open("tests/fixtures/file1_2_nested_diff.json") as f:
        data = json.loads(f.read())
    return data


def test_format(file1_2_nested_diff, file1_2_nested_plain):
    data = file1_2_nested_diff
    result = format(data)
    assert result == file1_2_nested_plain
