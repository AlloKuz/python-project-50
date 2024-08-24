from gendiff.utils.parse_file import parse_file


def test_parse_file():
    filepath = "tests/fixtures/make_diff_data_1.json"
    expected = {"host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False}
    assert parse_file(filepath) == expected
