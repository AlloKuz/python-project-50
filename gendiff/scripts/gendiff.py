from gendiff.utils.parse_file import parse_file
from gendiff.utils.cli import parse_args
from gendiff.utils.stringify import stringify


def make_diff(data1, data2):

	result_data = []

	common_keys = set(data1) & set(data2)
	added_keys = set(data2) - set(data1)
	removed_keys = set(data1) - set(data2)

	for key in added_keys:
		result_data.append({
			"name": key,
			"state": "added",
			"value": data2[key]
			})

	for key in removed_keys:
		result_data.append({
			"name": key,
			"state": "removed",
			"value": data1[key]
			})

	for key in common_keys:
		result_data.append({
			"name": key,
			"state": "changed",
			"value": [
				data1[key],
				data2[key]
				]
			})

	return result_data


PREFIX_ADDED = "+"
PREFIX_REMOVED = "-"
PREFIX_NONE = " "


def format_diff(data):
	result = {}


	def get_item_name(name, *, prefix=PREFIX_NONE):
		return f"{prefix} {name}"

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
	return dict(sorted(data_dict.items(), key=lambda x: x[0][len(PREFIX_NONE) + 1:]))


def main():
    args = parse_args()
    result = make_diff(parse_file(args.first_file), parse_file(args.second_file))
    result_string = stringify(sort_diff(format_diff(result)))
    print(result_string)


if __name__ == "__main__":
    main()
