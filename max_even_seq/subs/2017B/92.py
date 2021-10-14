def max_even_seq(n):
	ans = 0
	counter= 0
	num = str(n)
	for a in num:
		if int(a)%2 == 0:
			counter = counter+1
		else:
			if counter>ans:
				ans = counter
				counter = 0
			else:
				counter = 0
	if counter>ans:
		ans = counter
	return ans



