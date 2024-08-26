from .utils.make_json_diff import make_json_diff


JSON_WORDS = {
    True: "true",
    False: "false",
    None: "null"
}


def is_dict(data):
    return isinstance(data, dict)


def prepare_value(value):
    if is_dict(value):
        return "{"
    elif isinstance(value, bool) or value is None:
        return JSON_WORDS[value]
    return value


def _format_stylish(data, indent_symbol=" ", indent_size=4, shift_size=2):

    def iter_(current_data, level=1):
        indent_size_counted = level * indent_size - shift_size

        if not is_dict(current_data):
            return current_data

        # final list with lines of changes
        result = []

        # prepare dict
        for key in current_data.keys():
            indent = indent_size_counted * indent_symbol
            key = key
            value = prepare_value(current_data[key])

            result_str = f"{indent}{key}: {value}"
            result.append(result_str)

            if not is_dict(current_data[key]):
                continue

            nested_result = iter_(current_data[key], level + 1)
            if nested_result:
                result.extend(nested_result)

            result.append(f"{indent}{shift_size * indent_symbol}}}")

        return result

    result = iter_(data)
    return "{\n" + "\n".join(result) + "\n}" if result else ""


def format(data, raw=False):
    prepared_data = make_json_diff(data)

    return prepared_data if raw else _format_stylish(prepared_data)
