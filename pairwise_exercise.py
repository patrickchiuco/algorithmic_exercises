def pairwise(array, k):
	"""
	Gets the indices of the elements that sum to the given
	number k. Ensures the lowest index is used by using
	.index()
	"""

	index_sum = 0

	# iterate through all the elements to check for pairs
	for index in range(0, len(array)):
		try:
			# continue if the element has already been considered a pair
			if array[index] is None:
				continue
			else:
				# find the index pair and get the lowest index possible
				second_index = array.index(k-array[index])

				# continue if we're going to use the same element
				if index == second_index:
					continue

				# add the indices to the sum
				index_sum += index
				index_sum += second_index

				# mark the indices as considered by turning them into None
				array[index] = None
				array[second_index] = None
		except ValueError:
			# continue if the pair for the current element is not found
			continue
	return index_sum

	
