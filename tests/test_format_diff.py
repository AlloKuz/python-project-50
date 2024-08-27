from gendiff.formatters import plain_formatter

import pytest
import json


@pytest.fixture
def test_sort_diff_data():
    with open("tests/fixtures/test_sort_diff_data.json") as f:
        data = json.load(f)
    return data


@pytest.fixture
def test_sort_diff_data_sorted():
    with open("tests/fixtures/test_sort_diff_data_sorted.json") as f:
        data = json.load(f)
    return data


def test_format_diff_plain():
    data = [{'name': 'one', 'state': 'added', 'value': 1},
            {'name': 'qwerty', 'state': 'removed', 'value': 2},
            {'name': 'nest',
             'state': 'nested',
             'children': [{"name": "three", "state": "added", "value": 1},
                          {"name": "abra",
                           "state": "added",
                           "value": {"three": "solo"}}]},
            {'name': 'two', 'state': 'removed', 'value': 2},
            {'name': 'three', 'state': 'changed', 'value': [3, 4]}]

    result = ["Property 'nest.abra' was added with value: [complex value]",
              "Property 'nest.three' was added with value: 1",
              "Property 'one' was added with value: 1",
              "Property 'qwerty' was removed",
              "Property 'three' was updated. From 3 to 4",
              "Property 'two' was removed"]

    assert plain_formatter(data, raw=True) == result
    assert plain_formatter({}) == {}
