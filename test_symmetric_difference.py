from symmetric_difference_exercise import symmetric_difference


"""
	Tests the results of symmetric difference for two inputs
"""
def test_basic():
	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4]])
	assert answer == [3,4,5]

	# tests for the correct number of elements in the resulting array
	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4]])
	assert len(answer) == 3

	#tests the result of symmetric difference for repeated elements (left)
	answer = symmetric_difference(None, None, [[1, 2, 3, 3], [5, 2, 1, 4]])
	assert answer == [3, 4, 5]

	answer = symmetric_difference(None, None, [[1, 2, 3, 3], [5, 2, 1, 4]])
	assert len(answer) == 3

	#tests the result of symmetric difference for repeated elements (right)
	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4, 5]])
	assert answer == [3, 4, 5]

	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4, 5]])
	assert len(answer) == 3

"""
	Tests the results of symmetric difference for three inputs
"""
def test_triple():
	answer = symmetric_difference(None, None, [[1, 2, 5], [2, 3, 5], [3, 4, 5]])
	assert answer == [1, 4, 5]

	# tests that the resulting array has the expected number of elements
	answer = symmetric_difference(None, None, [[1, 2, 5], [2, 3, 5], [3, 4, 5]])
	assert len(answer) == 3	

	# tests the results of symmetric difference for repeated elements (2nd and 3rd input)
	answer = symmetric_difference(None, None, [[1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]])
	assert answer == [1, 4, 5]

	# tests that the resulting array has the expected number of elements
	answer = symmetric_difference(None, None, [[1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]])
	assert len(answer) == 3	

"""
	Tests the results of symmetric difference for 4 inputs.
"""
def test_quadruple():
	# tests the results of symmetrid difference for repeated elements (1st, 3rd)
	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]])
	assert answer == [2, 3, 4, 6, 7]

	# tests the number of elements in the resulting arrray is as expected
	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]])
	assert len(answer) == 5	

"""
	Tests the results of symmetric difference for 5 inputs.
"""
def test_sextuple():
	# tests the results of symmetrid difference for repeated elements (1st, 3rd)
	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]])
	assert answer == [1, 2, 4, 5, 6, 7, 8, 9]

	# tests the number of elements in the resulting arrray is as expected
	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]])
	assert len(answer) == 8