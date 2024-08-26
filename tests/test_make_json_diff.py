from gendiff.formatters.utils.make_json_diff import (_get_item_name,
                                                     add_prefixes_recursive,
                                                     _sort_key,
                                                     make_json_diff)

import json
import pytest


def test__get_item_name():
    assert _get_item_name("value", prefix="+") == "+ value"
    assert _get_item_name("value", prefix="") == " value"
    assert _get_item_name("value") == "  value"
    assert _get_item_name("") == "  "


def test_add_prefixes_recursive():
    data = {"nested": {"value": 2}}
    result = {"  nested": {"  value": 2}}
    assert add_prefixes_recursive(data) == result
    assert add_prefixes_recursive("value") == "value"
    assert add_prefixes_recursive({}) == {}


def test__sort_key():
    data = {"name": "abc", "state": "added"}
    assert _sort_key(data) == ("abc", 1)

    data = {"name": "abc", "state": "removed"}
    assert _sort_key(data) == ("abc", 0)


@pytest.fixture
def file1_2_nested_diff():
    with open("tests/fixtures/file1_2_nested_diff.json") as f:
        return json.loads(f.read())


@pytest.fixture
def file1_2_nested_result():
    with open("tests/fixtures/file1_2_nested_result.json") as f:
        return json.loads(f.read())


def test_make_json_diff(file1_2_nested_diff, file1_2_nested_result):
    data = file1_2_nested_diff
    result = make_json_diff(data)
    assert result == file1_2_nested_result

    data = {}
    result = make_json_diff(data)
    assert result == {}
    
