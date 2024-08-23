import json

def parse_file(filename):
    with open(filename) as f:
        json_file = json.load(f)
    return json_file
