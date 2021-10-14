def max_even_seq(n):
	counter = 0
	max_sequence = 0
    
	for num in str(n):
		if int(num) % 2 == 0 :
			counter += 1
		else:
			counter = 0
		if counter > max_sequence :
			max_sequence = counter
	
	return (max_sequence)





