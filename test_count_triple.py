from count_triple_exercise import count_triple

def test_count_triple():
	# tests base case
	assert count_triple("abcXXXabc") == 1
	assert count_triple("xxxabyyyycd") == 3
	assert count_triple("XXXabc") == 1
	assert count_triple("XXXXabc") == 2
	assert count_triple("XXXXXabc") == 3
	assert count_triple("222abyyycdXXX") == 3
	assert count_triple("abYYYabXXXXXab") == 4
	assert count_triple("122abhhh2") == 1

	# test case where there is only a single character
	assert count_triple("a") == 0

	# test edge case where we're given an empty string
	assert count_triple("") == 0

	# tests case where there are no triples
	assert count_triple("abYYXabXXYXXab") == 0
	assert count_triple("abYYXabXXYXXab") == 0
	