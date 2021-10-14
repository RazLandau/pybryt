def max_even_seq(n):
	curr_cnt = 0
	last_max = 0
	if n == 0:
		return 1
	while (n > 0):
		digit = n % 10
		if (digit % 2 == 0):
			curr_cnt += 1
		else:
			if (curr_cnt > last_max):
				last_max = curr_cnt
			curr_cnt = 0
		n = n // 10
	return max (curr_cnt,last_max)

