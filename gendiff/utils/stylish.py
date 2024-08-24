from itertools import chain


def stylish(data, indent_symbol=" ", indent_size=4):
    def iter_(current_data, level=1):
        if not isinstance(current_data, dict):
            return f"{current_data}"

        string = ""

        for el in chain(current_data):
            string += f"{indent_symbol * indent_size * level}{el}: "
            if isinstance(current_data[el], dict):
                string += "{\n" + iter_(current_data[el], level + 1)
                string += f"{indent_symbol * indent_size * level}}}\n"
            else:
                string += f"{current_data[el]}\n"

        return string

    return f"{{\n{iter_(data)}}}"


def stylish_plain(data):
    if not data:
        return
    result_str = ""
    for el in data:
        result_str += f"{el}\n"
    return result_str
