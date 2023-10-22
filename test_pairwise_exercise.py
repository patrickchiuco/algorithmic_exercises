from pairwise_exercise import pairwise


"""
	Tests that the result of the pairwise function is as
	expected
"""
def test_pairwise():
	# check for usual case
	answer = pairwise([1, 4, 2, 3, 0, 5], 7)
	assert answer == 11

	# check that if a an elemenet is equal to k it is not considered
	answer = pairwise([1, 3, 2, 4], 4)
	assert answer == 1

	# check that the lowest index was used
	answer = pairwise([1, 1, 1], 2)
	assert answer == 1

	# check for elements at the edge of the list
	answer = pairwise([0, 0, 0, 0, 1, 1], 1)
	assert answer == 10
	
	# test for case where there are no elements to be checked
	answer = pairwise([], 100)
	assert answer == 0

