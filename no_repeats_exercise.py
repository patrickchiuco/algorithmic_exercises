import re

"""
	Swaps the element at index1 with the element
	at index2 at the given array
"""
def swap(index1, index2, array):
	# buffer for switching array elements
	buffer = array[index1]

	# actual switching of elements
	array[index1] = array[index2]
	array[index2] = buffer

"""
	Python implementation of Heap's algorithm
	https://en.wikipedia.org/wiki/Heap%27s_algorithm
"""
def heaps_algorithm(k, array, answers):
	if k == 1:
		answers.append(''.join(array))
	else:
		heaps_algorithm(k-1, array, answers)

		for index in range(0, k-1):
			if k % 2 == 0:
				swap(index, k-1, array)
			else:
				swap(0, k-1, array)
			heaps_algorithm(k-1, array, answers)

"""
	Main no_repeats function. Separates input into
	a list of characters then generates all possible
	permutations using heap's algorithm. Uses a regular
	expression to determine whether there are repeats
	in a given permutation or not. Returns the number
	of permutations without any repeats.
"""
def no_repeats(string_input):
	# turn input into list of characters
	list_input = list(string_input)
	answers = []

	# generate all possible permutations using heap's algorithm
	heaps_algorithm(len(list_input), list_input, answers)
	no_repeats = []

	# check which permutations do not have a repeating
	# element and store them in a list
	for permutation in answers:
		if re.search(r'(\w)\1+', permutation) is None:
			no_repeats.append(permutation)

	# return number of permutations without repeats
	return len(no_repeats)


