PREFIX_ADDED = "+"
PREFIX_REMOVED = "-"
PREFIX_NONE = " "


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
