from .utils.make_json_diff import make_json_diff

from itertools import chain


def _format_stylish(data, indent_symbol=" ", indent_size=4):
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
        return '\n'.join(strings) if data else data
    return f"{{\n{iter_(data)}\n}}" if data else data


def format(data, raw=False):
    prepared_data = make_json_diff(data)
    return prepared_data if raw else _format_stylish(prepared_data)
