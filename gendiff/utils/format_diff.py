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
