def update_inventory(arr1, arr2):
	"""
	Compares the given arr1 with arr2 updating the
	item in arr1 if it exists and adds the item into
	arr1 if it doesn't exist
	"""

	# turn arr1 into a dictionary for faster lookup
	current_inventory = {element[1]:element[0] for element in arr1}

	# iterate through all the elements in arr2 to check if it exists in
	# arr1. If it does, update the dictionary, else add it to the dictionary
	for item in arr2:
		if item[1] in current_inventory:
			current_inventory[item[1]] += item[0]
		else:
			current_inventory[item[1]] = item[0]

	# return the dictionary into a list
	updated_inventory = [[value, key] for key, value in current_inventory.items()]
	# sort the list by the item name
	sorted_inventory = sorted(updated_inventory, key= lambda item: item[1])
	return sorted_inventory
