PREFIX_ADDED = "+"
PREFIX_REMOVED = "-"
PREFIX_NONE = " "


def get_item_name(name, *, prefix=PREFIX_NONE):
    return f"{prefix} {name}"


def format_diff(data):
    result = {}
    for item in data:
        state_value = item["state"]
        prefix = PREFIX_NONE
        if state_value == "added":
            prefix = PREFIX_ADDED
        elif state_value == "removed":
            prefix = PREFIX_REMOVED
        elif state_value == "changed":
            value = item["value"]
            if value[0] == value[1]:
                item_name = get_item_name(item["name"])
                result[item_name] = value[0]
            else:
                item_name = get_item_name(item["name"], prefix=PREFIX_REMOVED)
                result[item_name] = value[0]
                item_name = get_item_name(item["name"], prefix=PREFIX_ADDED)
                result[item_name] = value[1]
            continue
        item_name = get_item_name(item["name"], prefix=prefix)
        result[item_name] = item["value"]
    return result


def sort_diff(data_dict):
    def _sort_func(key):
        sort_key_1 = 0 if key.startswith(PREFIX_REMOVED) else 1
        return sort_key_1, key[len(PREFIX_REMOVED) + 1:]
    return dict(sorted(data_dict.items(),
                key=lambda x: _sort_func(x[0])))
