import re

def swap(index1, index2, array):
	buffer = array[index1]
	array[index1] = array[index2]
	array[index2] = buffer

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

def no_repeats(string_input):
	list_input = list(string_input)
	answers = []
	heaps_algorithm(len(list_input), list_input, answers)
	no_repeats = []
	for permutation in answers:
		if re.search(r'(\w)\1+', permutation) is None:
			no_repeats.append(permutation)
	return len(no_repeats)


