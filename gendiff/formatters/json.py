import json


def format(data):
    """
    Returns dictionary of changes in JSON format.
    """
    return json.dumps({"root": data})
