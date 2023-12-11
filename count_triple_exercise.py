def count_triple(str_input):
	"""
	Counts the number of instances where
	a character appears thrice in a row.
	"""

	count = 0

	# iterate through the string one
	# character at a time
	for i in range(len(str_input) - 2):

		# check if the next two characters are
		# the same. If yes, add 1 to count.
		if str_input[i] == str_input[i+1] and str_input[i+1] == str_input[i+2]:
			count += 1
	return count
