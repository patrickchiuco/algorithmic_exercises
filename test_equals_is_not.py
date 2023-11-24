from equals_is_not_exercise import equals_is_not, equals_is_not2

def test_equals_is_not():
	# tests base case 
	assert equals_is_not("This is not") == False
	assert equals_is_not("noisxxnotyynotxisi") == True
	assert equals_is_not("isisnotnot") == True

	# tests base case false
	assert equals_is_not("This is notnot") == True
	assert equals_is_not("noisxxnotyynotxsi") == False
	assert equals_is_not("isnotis") == False
	assert equals_is_not("mis3notpotbotis") == False

	# tests edge case where non of the two substrings appear
	assert equals_is_not("xxxyyyzzzintint") == True
	assert equals_is_not("") == True

	
	# tests edge case where one of the not 
	# substrings is a different case
	assert equals_is_not("isisnotno7Not") == False
	
	


def test_equals_is_not2():
	# tests base case 
	assert equals_is_not2("This is not") == False
	assert equals_is_not2("noisxxnotyynotxisi") == True
	assert equals_is_not2("isisnotnot") == True

	# tests base case false
	assert equals_is_not2("This is notnot") == True
	assert equals_is_not2("noisxxnotyynotxsi") == False
	assert equals_is_not2("isnotis") == False
	assert equals_is_not2("mis3notpotbotis") == False
	
	# tests edge t where non of the two substrings appear
	assert equals_is_not2("xxxyyyzzzintint") == True
	assert equals_is_not2("") == True

	
	# tests edge case where one of the not 
	# substrings is a different case
	assert equals_is_not2("isisnotno7Not") == False
	