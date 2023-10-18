from symmetric_difference_exercise import symmetric_difference

def test_basic():
	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4]])
	assert answer == [3,4,5]

	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4]])
	assert len(answer) == 3

	answer = symmetric_difference(None, None, [[1, 2, 3, 3], [5, 2, 1, 4]])
	assert answer == [3, 4, 5]

	answer = symmetric_difference(None, None, [[1, 2, 3, 3], [5, 2, 1, 4]])
	assert len(answer) == 3

	#####
	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4, 5]])
	assert answer == [3, 4, 5]

	answer = symmetric_difference(None, None, [[1, 2, 3], [5, 2, 1, 4, 5]])
	assert len(answer) == 3

def test_triple():
	answer = symmetric_difference(None, None, [[1, 2, 5], [2, 3, 5], [3, 4, 5]])
	assert answer == [1, 4, 5]

	answer = symmetric_difference(None, None, [[1, 2, 5], [2, 3, 5], [3, 4, 5]])
	assert len(answer) == 3	

	answer = symmetric_difference(None, None, [[1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]])
	assert answer == [1, 4, 5]

	answer = symmetric_difference(None, None, [[1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]])
	assert len(answer) == 3	


def test_quadruple():
	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]])
	assert answer == [2, 3, 4, 6, 7]

	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]])
	assert len(answer) == 5	

def test_sextuple():
	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]])
	assert answer == [1, 2, 4, 5, 6, 7, 8, 9]

	answer = symmetric_difference(None, None, [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]])
	assert len(answer) == 8