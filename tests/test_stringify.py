from gendiff.utils.stringify import stringify


def test_stringify():
    data = {"one": 1, "two": 2}
    result = "{\n    one: 1\n    two: 2\n}"
    assert stringify(data) == result
    data = {"one": 1, "two": 2, "nested": {"three": 3, "nested": {"four" : 4}}}
    result = ("{\n    one: 1\n    two: 2\n    nested: {\n        three: 3\n" + 
            "        nested: {\n            four: 4\n        }\n    }\n}")
    assert stringify(data) == result
