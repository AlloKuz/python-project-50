import json
import yaml
import os


def parse(data, format="json"):
    if format == "json":
        return json.loads(data)
    elif format in ("yml", "yaml"):
        return yaml.safe_load(data)
    else:
        raise ValueError("Wrong format!")
    return None


def get_content(filename):

    ext = os.path.splitext(filename)[-1].replace(".", "")

    if not filename or not os.path.isfile(filename):
        raise ValueError(f"File '{filename}' does not exists!")

    with open(filename) as f:
        content = f.read()

    data = parse(content, ext)

    return data
