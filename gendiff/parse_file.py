import json
import yaml


def parse_file(filename):
    data = None
    if filename.endswith("json"):
        with open(filename) as f:
            data = json.load(f)
    elif filename.endswith("yml") or filename.endswith("yaml"):
        with open(filename) as f:
            data = yaml.safe_load(f)
    else:
        raise ValueError(f"Wrong exception at `{filename}`")
    return data
