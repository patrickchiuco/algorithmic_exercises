from no_repeats_exercise import no_repeats


"""
	Tests that the no repeats function produces
	the desired result.
"""
def test_pairwise():
	# checks that no_repeats returns a number
	answer = no_repeats('aab')
	assert type(answer) is int

	# checks that no_repeats returns the expected
	# answer for the usual case
	answer = no_repeats('aab')
	assert answer == 2

	# checks that no_repeats returns 0 when all
	# characters are the same
	answer = no_repeats('aaa')
	assert answer == 0

	answer = no_repeats('aabb')
	assert answer == 8
	
	# checks that no_repeats returns the correct result
	# when all characters are unique
	answer = no_repeats('abcdefa')
	assert answer == 3600

	answer = no_repeats('abfdefa')
	assert answer == 2640

	answer = no_repeats('zzzzzzzz')
	assert answer == 0

	# checks for edge case where there is only one character
	answer = no_repeats('a')
	assert answer == 1

	answer = no_repeats('aaab')
	assert answer == 0

	answer = no_repeats('aaabb')
	assert answer == 12
