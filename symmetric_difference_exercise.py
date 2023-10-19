"""
	Gets the symmetric difference of two sets.
	Subtracts the interection from the set union to get
	the elements unique for each set.
"""
def get_symmetric_difference(set1, set2):
	answer = []
	# get union of both sets
	set_union = set1.union(set2)
	# get interesection of the two sets
	set_intersection = set1.intersection(set2)

	# return the set union without the intersecting elements
	return set_union.difference(set_intersection)

	
"""
	Gets the symmetric difference of a group of arrays.
	Gets the symmetric difference of the first two elements, then uses
	the answer as the first argument to get_symmetric_difference
	with the next element in num_list as the second argument.
"""
def symmetric_difference(set1, set2, num_list):
	if set1 is not None and len(num_list) == 0:
		# if set1 is not None and there are no elements left in num_list,
		# final answer has been received
		return list(set1)
	elif set1 is None and set2 is None:
		# if both set 1 and set 2 are None, it is just the start of the computation
		# get the first two elements of num_list and get the symmetric difference
		set1 = set(num_list.pop(0))
		set2 = set(num_list.pop(0))
		answer = get_symmetric_difference(set1, set2)
		return symmetric_difference(answer, None, num_list)
	elif set1 is not None and set2 is None:
		# if set1 is not None and set2 is None, a previous computation for symmetric
		# difference has been done. Get the next element in num_list and get the symmetric
		# difference for the previous calculation and the next element in num_list
		set2 = set(num_list.pop(0))
		answer = get_symmetric_difference(set1, set2)
		return symmetric_difference(answer, None, num_list)




