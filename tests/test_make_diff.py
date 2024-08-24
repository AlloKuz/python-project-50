from gendiff.utils.make_diff import *

import json
import pytest



@pytest.fixture
def make_test_data_1():
    with open("tests/fixtures/make_diff_data_1.json") as f:
        result = json.load(f)
    return result


@pytest.fixture
def make_test_data_2():
    with open("tests/fixtures/make_diff_data_2.json") as f:
        result = json.load(f)
    return result


@pytest.fixture
def make_test_result():
    with open("tests/fixtures/make_diff_result.json") as f:
        result = json.load(f)
    return result


@pytest.fixture
def make_format_diff_str():
    with open("tests/fixtures/make_format_diff_result.json") as f:
        result = json.load(f)
    return result


def test_make_diff(make_test_data_1, make_test_data_2, make_test_result):
    def _sort_by_name(data):
        return sorted(data, key=lambda x: x['name'])
    result = make_diff(make_test_data_1, make_test_data_2)
    result = _sort_by_name(result)
    make_test_result = _sort_by_name(make_test_result)
    assert result == make_test_result
    assert make_diff({}, {}) == []


def test_make_and_format_diff(make_test_data_1, make_test_data_2, make_format_diff_str):
    result = make_and_format_diff(make_test_data_1, make_test_data_2)
    assert result == make_format_diff_str
    assert make_and_format_diff({}, {}) == {}
