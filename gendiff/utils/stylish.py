from itertools import chain
import json


def stylish(data, indent_symbol=" ", indent_size=4):
    def iter_(current_data, level=1):
        if not isinstance(current_data, dict):
            return f"{current_data}"

        strings = []

        for el in chain(current_data):
            strings.append(f"{indent_symbol * indent_size * level}{el}: ")
            if isinstance(current_data[el], dict):
                strings[-1] += "{"
                strings.append(iter_(current_data[el], level + 1))
                strings.append(f"{indent_symbol * indent_size * level}")
                strings[-1] += "}"
            else:
                strings[-1] += f"{current_data[el]}"
        return '\n'.join(strings)

    return f"{{\n{iter_(data)}\n}}"


def stylish_plain(data):
    if not data:
        return
    result_str = ""
    for el in data:
        result_str += f"{el}\n"
    return result_str


def json_formatter(data):
    return json.dumps(data)
