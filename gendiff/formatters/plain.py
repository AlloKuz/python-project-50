import json


def _get_name(name, path):
    if not path:
        return name
    return f"{path}.{name}"


def _replace_complex_with_text(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    return json.dumps(value)


def _format_diff(data, *, path=''):
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
                value = _replace_complex_with_text(item["value"])
                item_string = templates_dict["added"].format(name=item_name,
                                                             value=value)
                result.append(item_string)

            case "removed":
                item_name = _get_name(item["name"], path)
                value = _replace_complex_with_text(item["value"])
                temp = templates_dict["removed"]
                item_string = temp.format(name=item_name,
                                          value=value)
                result.append(item_string)

            case "changed":
                item_name = _get_name(item["name"], path)
                old_value = _replace_complex_with_text(item["value"][0])
                new_value = _replace_complex_with_text(item["value"][1])
                temp = templates_dict["updated"]
                item_string = temp.format(name=item_name,
                                          old_value=old_value,
                                          new_value=new_value)
                result.append(item_string)

            case "nested":
                item_name = _get_name(item["name"], path)

                result.extend(_format_diff(item["children"],
                                           path=item_name))
    return sorted(result)


def format(data, raw=False):
    prepared_data = _format_diff(data)

    if not prepared_data:
        return data

    if raw:
        return prepared_data

    result_str = ""
    for el in prepared_data:
        result_str += f"{el}\n"
    return result_str