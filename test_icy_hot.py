from icy_hot_exercise import icy_hot

def test_icy_hot():
	# tests basic case where temp1 > 100 and temp2 < 0
	assert icy_hot(120, -1) is True
	
	# tests case where temp1 < 0 and temp2 > 100
	assert icy_hot(-1, 120) is True

	# tests case where temp1 > 0 but temp2 > 100
	assert icy_hot(2, 120) is False
	
	# tests case where temp1 < 0 but temp2 == 100
	assert icy_hot(-1, 100) is False
	
	# tests case where both temp1 and temp2 are < 0
	assert icy_hot(-2, -2) is False
	
	# tests case where both temp1 and temp2 are > 100
	assert icy_hot(120, 120) is False
