def prepare_value(value):
    if isinstance(value, dict):
        return "{"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return value


def iter_(current_data, level=1, *, indent_symbol, indent_size, shift_size):
    indent_size_counted = level * indent_size - shift_size

    if not isinstance(current_data, dict):
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

        if isinstance(current_data[key], dict):

            nested_result = iter_(current_data[key],
                                  level + 1,
                                  indent_symbol=indent_symbol,
                                  indent_size=indent_size,
                                  shift_size=shift_size)
            if nested_result:
                result.extend(nested_result)

            result.append(f"{indent}{shift_size * indent_symbol}}}")

    return result


def format(data, raw=False, *,
           indent_symbol=" ", indent_size=4, shift_size=2):
    if raw:
        return data
    result = iter_(data,
                   indent_symbol=indent_symbol,
                   indent_size=indent_size,
                   shift_size=shift_size)
    return "{\n" + "\n".join(result) + "\n}" if result else ""
