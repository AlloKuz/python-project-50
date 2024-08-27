INDENT_SYMBOL = " "
INDENT_SIZE = 4
SHIFT_SIZE = 2


def prepare_value(value):
    if isinstance(value, dict):
        return "{"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return value


def iter_(current_data, level=1):
    indent_size_counted = level * INDENT_SIZE - SHIFT_SIZE

    if not isinstance(current_data, dict):
        return current_data

    # final list with lines of changes
    result = []

    # prepare dict
    for key in current_data.keys():
        indent = indent_size_counted * INDENT_SYMBOL
        key = key
        value = prepare_value(current_data[key])

        result_str = f"{indent}{key}: {value}"
        result.append(result_str)

        if isinstance(current_data[key], dict):

            nested_result = iter_(current_data[key],
                                  level + 1)
            if nested_result:
                result.extend(nested_result)

            result.append(f"{indent}{SHIFT_SIZE * INDENT_SYMBOL}}}")

    return result


def format(data):
    result = iter_(data)
    return "{\n" + "\n".join(result) + "\n}" if result else ""
