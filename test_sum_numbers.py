from sum_numbers_exercise import sum_numbers, sum_numbers2

def test_sum_numbers():
	# tests base case
	assert sum_numbers("abc123xyz") == 123	
	assert sum_numbers("aa11b33") == 44	
	assert sum_numbers("7 11") == 18	
	assert sum_numbers("5hoco1a1e") == 7	
	assert sum_numbers("5$$1;;1!!") == 7	
	assert sum_numbers("a1234bb11") == 1245	
	assert sum_numbers("a22bbb3") == 25	

	# tests egde case where there are no numbers
	assert sum_numbers("Chocolate") == 0

	# tests edge case where we're given an empty string
	assert sum_numbers("") == 0
	


def test_sum_numbers2():
	# tests base case
	assert sum_numbers2("abc123xyz") == 123	
	assert sum_numbers2("aa11b33") == 44	
	assert sum_numbers2("7 11") == 18	
	assert sum_numbers2("5hoco1a1e") == 7	
	assert sum_numbers2("5$$1;;1!!") == 7	
	assert sum_numbers2("a1234bb11") == 1245	
	assert sum_numbers2("a22bbb3") == 25	

	# tests egde case where there are no numbers
	assert sum_numbers2("Chocolate") == 0

	# tests edge case where we're given an empty string
	assert sum_numbers2("") == 0	
