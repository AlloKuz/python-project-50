from .utils.make_json_diff import make_json_diff


JSON_WORDS = {
    True: "true",
    False: "false",
    None: "null"
}


def _format_stylish(data, indent_symbol=" ", indent_size=4, shift_size=2):

    def iter_(current_data, level=1):
        indent_size_counted = level * indent_size - shift_size

        if not isinstance(current_data, dict):
            return current_data

        # final list with lines of changes
        result = []

        # prepare dict
        for key in current_data.keys():
            indent = indent_size_counted * indent_symbol
            key = key
            if isinstance(current_data[key], dict):
                value = "{"
            else:
                value = current_data[key]
                if value in JSON_WORDS:
                    value = JSON_WORDS[value]
            result_str = f"{indent}{key}: {value}"
            result.append(result_str)

            if isinstance(current_data[key], dict):
                nested_result = iter_(current_data[key], level + 1)
                if nested_result:
                    result.extend(nested_result)

                result.append(f"{indent}{shift_size * indent_symbol}}}")

        return result

    result = iter_(data)
    if result:
        return ["{"] + result + ["}"]
    return data


def format(data, raw=False):
    prepared_data = make_json_diff(data)

    return prepared_data if raw else '\n'.join(_format_stylish(prepared_data))
