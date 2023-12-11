from count_clumps_exercise import count_clumps

def test_count_clumps():

	# tests general case
	assert count_clumps([1, 2, 2, 3, 4, 4]) == 2	
	assert count_clumps([1, 1, 2, 1, 1]) == 2	
	assert count_clumps([2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 4	
	assert count_clumps([0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 4	
	assert count_clumps([0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 5	
	assert count_clumps([0, 0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 5

	# tests edge case where we have one large clump
	assert count_clumps([1, 1, 1, 1, 1]) == 1

	# tests edge case where we have no clumps	
	assert count_clumps([1, 2, 3]) == 0	

	# tests edge case where the given is of length 0 
	assert count_clumps([]) == 0 