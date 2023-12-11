def count_clumps(str_input):
	"""
	Returns the number of clumps (continuously
	appearing characters in a given string)
	"""

	# Flag used to see if we one large clump
	has_changed = False
	# Buffer used to check if we have a clump  
	buffer = ""  
	changes = 0
	i = 0

	# parse the given string checking for
	# times when the character changes.
	# Add the character to buffer if it's
	# the same for us to check if there is a 
	# clump.
	while i < len(str_input) - 1:
		if str_input[i] == str_input[i+1]:
			buffer += str(str_input[i])
		else:
			# change has_changed to True if the
			# character changes. Add the current
			# character to buffer and check if it's
			# a clump. Reset buffer afterwards.
			has_changed = True
			buffer += str(str_input[i])
			if len(buffer) >= 2:
				changes += 1
			buffer = ""
		i += 1

	if len(str_input) > 0:
		# add to buffer the last value in 
		# str_input since it wont be added
		# because of the condition
		buffer += str(str_input[i])
	
	if len(buffer) >= 2 and has_changed:
		# check if buffer has characters left
		# meaning the clump is at the end.
		# increase changes by one.
		changes += 1
	elif not has_changed and len(str_input) > 0:
		# if has_changed is False and the input
		# length is more than one, increase
		# changes by one meaning we have one big
		# clump.
		changes += 1
	return changes