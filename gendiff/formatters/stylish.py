INDENT_SYMBOL = " "
INDENT_SIZE = 4
SHIFT_SIZE = 2


def prepare_value(value, *, level=1):
    if isinstance(value, dict):
        result = [""]

        nested_result = []
        # prepare dict
        for key in value.keys():
            indent = (level * INDENT_SIZE - SHIFT_SIZE) * INDENT_SYMBOL
            new_value = prepare_value(value[key], level=level + 1)

            result_str = f"{indent}{key}: {new_value}"
            nested_result.append(result_str)

        if nested_result:
            closing_bracket_str = f"{indent[:-SHIFT_SIZE]}}}"

            result[-1] += "{"
            result.extend(nested_result)
            result.append(f"{closing_bracket_str}")

        return "\n".join(result)

    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return value


def format(data):
    result = prepare_value(data)
    return result
    return "{\n" + "\n".join(result) + "\n}" if result else ""
