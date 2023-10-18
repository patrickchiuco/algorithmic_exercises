"""
	Gets the symmetric difference of two sets.
	Checks if each element in the set is in the intersection,
	if not, add to the answer list.
"""
def get_symmetric_difference(set1, set2):
	answer = []
	# get interesection of the two sets
	set_intersection = set1.intersection(set2)

	# check if which elements are not in the intersection,
	# add them to the answer list
	for element in set1:
		if element not in set_intersection:
			answer.append(element)
	for element in set2:
		if element not in set_intersection:
			answer.append(element)
	return set(answer)


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




