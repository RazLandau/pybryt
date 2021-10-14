def max_even_seq(n):
	counter=0
	mx=0
	n=str(n)
	for i in range(len(n)):
		if int(n[i])%2==0:
			counter+=1
		else:
			counter=0
		if counter>mx:
			mx=counter

	return (mx)
	
