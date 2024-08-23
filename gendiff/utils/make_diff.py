from gendiff.utils.format_diff import format_diff, sort_diff


def make_diff(data1, data2):
    result_data = []
    common_keys = set(data1) & set(data2)
    added_keys = set(data2) - set(data1)
    removed_keys = set(data1) - set(data2)

    for key in added_keys:
        result_data.append({
            "name": key,
            "state": "added",
            "value": data2[key]})

    for key in removed_keys:
        result_data.append({
            "name": key,
            "state": "removed",
            "value": data1[key]})

    for key in common_keys:
        result_data.append({
            "name": key,
            "state": "changed",
            "value": [
                data1[key],
                data2[key]]})

    return result_data


def make_and_format_diff(data1, data2):
    return sort_diff(format_diff(make_diff(data1, data2)))
