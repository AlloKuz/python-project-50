from gendiff.utils.format_diff import *

import pytest

def test_get_item_name():
    assert get_item_name("test", prefix="+") == "+ test"
    assert get_item_name("test") == "  test"
    assert get_item_name("test", prefix="") == " test"
    assert get_item_name("", prefix="+") == "+ "


def test_sort_diff():
    data = {
        "+ one": 2,
        "  two": 1,
        "+ three": 2,
        "- four": 2,
        "  five": 3,
        "- three": 3,
        "- one": 1,
    }
    result = {
        "- four": 2,
        "  five": 3,
        "- one": 1,
        "+ one": 2,
        "  two": 1,
        "- three": 3,
        "+ three": 2,
    }
    assert sort_diff(data) == result
    assert sort_diff({}) == {}


def test_format_diff():
    data = [{'name': 'one', 'state': 'added', 'value': 1},
            {'name': 'two', 'state': 'removed', 'value': 2},
            {'name': 'three', 'state': 'changed', 'value': [3, 4]}]
    result = {
        "+ one": 1,
        "- three": 3,
        "+ three": 4,
        "- two": 2,
    }
    assert format_diff(data) == result
    assert format_diff({}) == {}
