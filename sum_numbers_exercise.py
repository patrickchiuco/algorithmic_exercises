import re

"""
	Returns the sum of all the numbers in the given
	string. Uses regex to find all numbers then
	sums them up.
"""
def sum_numbers(str_input):
	# find all instances ofnumbers in the given
	# string 
	all_numbers = re.findall(r'\d+', str_input)
	sum = 0

	# sum all the number instances found in
	# the string
	for num in all_numbers:
		sum += int(num)
	return sum

"""
	Finds all the number instances in the string
	iteratively. Returns the sum of those numbers.
"""
def sum_numbers2(str_input):
	all_nums = []
	buffer = ""
	i = 0

	# iterate through the string
	while i < len(str_input):

		# add the buffer if the current character is a digit.
		if str_input[i].isdigit():
			buffer += str_input[i]
		else:

			# else check if we have buffered characters. If
			# yes add them to the list.
			if buffer != "":
				all_nums.append(int(buffer))

			# reset buffer whenever we find a number
			buffer = ""
		i += 1

	# add the last number in the string if there is one
	if buffer != "":
		all_nums.append(int(buffer))
	
	return sum(all_nums)