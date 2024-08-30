import json
import yaml
import os


def parse(data, format="json"):
    """
    Attempts to load data depending on the format.
    If the format is incorrect, the function raises an exception.
    """
    if format == "json":
        return json.loads(data)
    elif format in ("yml", "yaml"):
        return yaml.safe_load(data)
    raise ValueError("Wrong format! Needs: json/yaml file!")


def get_content(filename):
    """
    Reads the contents of the file and returns the loaded data,
    using the file extension to determine the format.
    """

    with open(filename) as f:

        _, ext = os.path.splitext(filename)

        data = parse(f.read(), ext[1:])

    return data
