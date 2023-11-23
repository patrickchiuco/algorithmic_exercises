import re

"""
	Returns true if the instances of the substring 'is'
	is equal to the instances of the substring 'not'
"""
def equals_is_not(str_input):
	# use regex to find all instances of the substrings
	all_is = re.findall(r'(is)', str_input)
	all_not = re.findall(r'(not)', str_input)

	# return true if the instances of both are equal else false
	return len(all_is) == len(all_not)


"""
	Counts the instances of the substring 'is' and 'not'
	iteratively.
"""
def count_instances(str_input, needle):
	try:
		# mark the start of the substring to be considered
		start_index = 0

		# find the substring to be considered
		end_index = str_input.index(needle, start_index)
		count = 0

		# while we haven't considered the whole string iterate
		# and move the markers
		while start_index < len(str_input):
			try:
				count += 1

				# move the starting marker to the start of the appea-
				# rance of the needle plus the needle length to avoid
				# including parts of the needle
				start_index = end_index + len(needle)

				# find the next occurence of the needle from the new
				# start index marker
				end_index = str_input.index(needle, start_index)
			except ValueError:

				# if the needle cannot be found, return the current count
				return count
	except ValueError:
		# if the substring cannot be found return 0
		return 0


"""
	Returns true if the instances of the substring 'is'
	is equal to the instances of the substring 'not' by
	counting iteratively.
"""
def equals_is_not2(str_input):
	is_instances = count_instances(str_input, 'is')
	not_instances = count_instances(str_input, 'not')
	return is_instances == not_instances

