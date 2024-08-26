from gendiff.utils.format_diff import format_diff


def _prepare_data_item(name, state, value, is_nested=False):
    return {"name": name,
            "state": state,
            "children" if is_nested else "value": value}


def make_diff(data1, data2):
    result_data = []

    added_keys = set(data2) - set(data1)

    all_keys = set(data1) | set(data2)

    nested_keys = set()

    def _sort_key(data):
        return data['name'], (0 if data['state'] == "removed" else 1)

    for key in all_keys:
        # check if nested
        if key in all_keys:
            if all(isinstance(x.get(key), dict) for x in (data1, data2)):
                nested_keys.add(key)

        if key in all_keys - nested_keys:
            data_by_status = {
                "added": data2.get(key, None),
                "removed": data1.get(key, None),
                "notchanged": data1.get(key, None),
                "changed": [data1.get(key, None), data2.get(key, None)]}

            current_status = None
            if key in set(data1) ^ set(data2):
                current_status = "added" if key in added_keys else "removed"
            else:
                current_status = ("notchanged"
                                  if (data1[key] == data2[key])
                                  else "changed")

            new_data = _prepare_data_item(key,
                                          current_status,
                                          data_by_status[current_status])

            result_data.append(new_data)

        if key in nested_keys:
            new_data = make_diff(data1[key], data2[key])
            result_data.append(_prepare_data_item(key,
                                                  "nested",
                                                  new_data,
                                                  is_nested=True))
    result_data.sort(key=_sort_key)
    return result_data


def make_and_format_diff(data1, data2):
    return format_diff(make_diff(data1, data2))
