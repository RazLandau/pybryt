def max_even_seq(n):
		n = str(n)
		m = 0
		cnt = 0
		for i in n:
			if int(i) % 2 == 0:
					cnt = cnt + 1
					m = max(m,cnt)
			else:
					cnt = 0
		return(m)






