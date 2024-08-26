import json
import yaml


def parse(data, format):
    if format == "yml":
        format = "yaml"

    match format:
        case "json":
            return json.loads(data)
        case "yaml":
            return yaml.safe_load(data)
        case _:
            raise ValueError("Wrong format!")
    return None


def get_file_content(filename):
    with open(filename) as f:
        data = f.read()
    return data


def parse_by_filename(filename):
    if filename.endswith('json'):
        filetype = "json"
    elif filename.endswith("yaml") or filename.endswith("yml"):
        filetype = "yaml"
    else:
        raise ValueError("Wrong file extension!")
    content = get_file_content(filename)

    data = parse(content, filetype)
    return data
