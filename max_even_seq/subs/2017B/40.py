def max_even_seq(n):
	a=0
	while n>0:
		if ((n%10)%2==0):
			b=1
			n=n//10
			a=max(a,b)
			while n>0 and (n%10)%2==0:
				b=b+1
				a=max(a,b)
				n=n//10
		else:
			n=int(n//10)
	return a





