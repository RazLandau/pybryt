def max_even_seq(n):
	max = 0
	current_sequance = 0
	for digit in str(n):
		if int(digit)%2 == 0:
			current_sequance += 1
			if current_sequance > max:
				max = current_sequance
		else:
			current_sequance = 0
	return max

