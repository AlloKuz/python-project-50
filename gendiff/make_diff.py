def _prepare_data_item(name, state, value, is_nested=False):
    return {"name": name,
            "state": state,
            "children" if is_nested else "value": value}


def make_diff(data1, data2):

    result_data = []

    added_keys = set(data2) - set(data1)

    removed_keys = set(data1) - set(data2)

    all_keys = set(data1) | set(data2)

    for key in all_keys:
        # check if nested
        if all(isinstance(x.get(key), dict) for x in (data1, data2)):
            new_data = make_diff(data1[key], data2[key])
            result_data.append(_prepare_data_item(key,
                                                  "nested",
                                                  new_data,
                                                  is_nested=True))
            continue

        data_by_status = {
            "added": data2.get(key, None),
            "removed": data1.get(key, None),
            "notchanged": data1.get(key, None),
            "changed": [data1.get(key, None), data2.get(key, None)]}

        current_status = None
        if key in added_keys:
            current_status = "added"
        elif key in removed_keys:
            current_status = "removed"
        else:
            current_status = ("notchanged"
                              if (data1[key] == data2[key])
                              else "changed")

        new_data = _prepare_data_item(key,
                                      current_status,
                                      data_by_status[current_status])

        result_data.append(new_data)

    return result_data
