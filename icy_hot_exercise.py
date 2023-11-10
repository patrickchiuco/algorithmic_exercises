def icy_hot(temp1, temp2):
	"""
		Returns true if one temp is < 0 and the other temp is > 100
	"""
	return (temp1 < 0 and temp2 > 100) or (temp1 > 100 and temp2 < 0)	
