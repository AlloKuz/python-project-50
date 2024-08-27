PREFIX_ADDED = "+"
PREFIX_REMOVED = "-"
PREFIX_NONE = " "

INDENT_SYMBOL = " "
INDENT_SIZE = 4
SHIFT_SIZE = 2


def _get_item_name(name, *, prefix=PREFIX_NONE):
    return f"{prefix} {name}"


def add_prefixes_recursive(data):
    if isinstance(data, dict):
        new_dict = dict()
        for k in data.keys():
            new_key = _get_item_name(k)
            new_dict[new_key] = add_prefixes_recursive(data[k])
        return new_dict
    return data


def _sort_key(data):
    return data['name'], (0 if data['state'] == "removed" else 1)


def make_json_diff(data):

    result = {}

    data = sorted(data, key=_sort_key)

    for item in data:
        state_value = item["state"]

        match state_value:

            case "added":
                item_name = _get_item_name(item["name"], prefix=PREFIX_ADDED)
                value = add_prefixes_recursive(item["value"])
                result[item_name] = value

            case "removed":
                item_name = _get_item_name(item["name"], prefix=PREFIX_REMOVED)
                value = add_prefixes_recursive(item["value"])
                result[item_name] = value

            case "notchanged":
                item_name = _get_item_name(item["name"], prefix=PREFIX_NONE)
                value = add_prefixes_recursive(item["value"])
                result[item_name] = value

            case "changed":
                item_name = _get_item_name(item["name"], prefix=PREFIX_REMOVED)
                value = add_prefixes_recursive(item["value"][0])
                result[item_name] = value

                item_name = _get_item_name(item["name"], prefix=PREFIX_ADDED)
                value = add_prefixes_recursive(item["value"][1])
                result[item_name] = value

            case "nested":
                item_name = _get_item_name(item["name"], prefix=PREFIX_NONE)
                result[item_name] = make_json_diff(item["children"])

    return result


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
    result = prepare_value(make_json_diff(data))
    return result
