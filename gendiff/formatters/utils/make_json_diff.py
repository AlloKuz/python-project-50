PREFIX_ADDED = "+"
PREFIX_REMOVED = "-"
PREFIX_NONE = " "


def _get_item_name(name, *, prefix=PREFIX_NONE):
    return f"{prefix} {name}"


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
                result[item_name] = item["value"]

            case "removed":
                item_name = _get_item_name(item["name"], prefix=PREFIX_REMOVED)
                result[item_name] = item["value"]

            case "notchanged":
                item_name = _get_item_name(item["name"], prefix=PREFIX_NONE)
                result[item_name] = item["value"]

            case "changed":
                item_name = _get_item_name(item["name"], prefix=PREFIX_REMOVED)
                result[item_name] = item["value"][0]

                item_name = _get_item_name(item["name"], prefix=PREFIX_ADDED)
                result[item_name] = item["value"][1]

            case "nested":
                item_name = _get_item_name(item["name"], prefix=PREFIX_NONE)
                result[item_name] = make_json_diff(item["children"])

    return result
