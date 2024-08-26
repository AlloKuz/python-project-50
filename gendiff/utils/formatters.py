import json


PREFIX_ADDED = "+"
PREFIX_REMOVED = "-"
PREFIX_NONE = " "


def get_item_name(name, *, prefix=PREFIX_NONE):
    return f"{prefix} {name}"


def format_diff_json(data):
    result = {}

    for item in data:
        state_value = item["state"]

        match state_value:

            case "added":
                item_name = get_item_name(item["name"], prefix=PREFIX_ADDED)
                result[item_name] = item["value"]

            case "removed":
                item_name = get_item_name(item["name"], prefix=PREFIX_REMOVED)
                result[item_name] = item["value"]

            case "notchanged":
                item_name = get_item_name(item["name"], prefix=PREFIX_NONE)
                result[item_name] = item["value"]

            case "changed":
                item_name = get_item_name(item["name"], prefix=PREFIX_REMOVED)
                result[item_name] = item["value"][0]
                item_name = get_item_name(item["name"], prefix=PREFIX_ADDED)
                result[item_name] = item["value"][1]

            case "nested":
                item_name = get_item_name(item["name"], prefix=PREFIX_NONE)
                result[item_name] = format_diff_json(item["children"])
    return result


def _get_name(name, path):
    if not path:
        return name
    return f"{path}.{name}"


def replace_complex_with_text(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    return json.dumps(value)


def format_diff_plain(data, path=''):
    result = []

    templates_dict = {
        "added":
            "Property '{name}' was added with value: {value}",
        "removed":
            "Property '{name}' was removed",
        "updated":
            "Property '{name}' was updated. From {old_value} to {new_value}"
    }

    for item in data:
        item_string = ""
        state_value = item["state"]

        match state_value:

            case "added":
                item_name = _get_name(item["name"], path)
                value = replace_complex_with_text(item["value"])
                item_string = templates_dict["added"].format(name=item_name,
                                                             value=value)
                result.append(item_string)

            case "removed":
                item_name = _get_name(item["name"], path)
                value = replace_complex_with_text(item["value"])
                temp = templates_dict["removed"]
                item_string = temp.format(name=item_name,
                                          value=value)
                result.append(item_string)

            case "changed":
                item_name = _get_name(item["name"], path)
                old_value = replace_complex_with_text(item["value"][0])
                new_value = replace_complex_with_text(item["value"][1])
                temp = templates_dict["updated"]
                item_string = temp.format(name=item_name,
                                          old_value=old_value,
                                          new_value=new_value)
                result.append(item_string)

            case "nested":
                item_name = _get_name(item["name"], path)
                result.extend(format_diff_plain(item["children"],
                                                path=item_name))
    return sorted(result)
