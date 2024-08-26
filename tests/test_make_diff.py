from gendiff.make_diff import make_diff

import pytest
import yaml
import json


@pytest.fixture
def file1_nested():
    with open("tests/fixtures/file1_nested.yaml") as f:
        data = yaml.safe_load(f.read())
    return data


@pytest.fixture
def file2_nested():
    with open("tests/fixtures/file2_nested.yaml") as f:
        data = yaml.safe_load(f.read())
    return data


@pytest.fixture
def file1_2_nested_diff():
    with open("tests/fixtures/file1_2_nested_diff.json") as f:
        data = json.loads(f.read())
    return data


def test_make_diff(file1_nested, file2_nested, file1_2_nested_diff):
    result = make_diff(file1_nested, file2_nested)
    assert result == file1_2_nested_diff
