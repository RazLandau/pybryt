def max_even_seq(n):
    sn=str(n)
	lst=[]
	l=[]
	for i in range(len(sn)):
		lst.append(sn[i])
	for j in range(len(lst)):
		if eval(lst[j])%2==0:
			l.append(eval(lst[j]))
		else:
			l.append("e")
	return l



    




