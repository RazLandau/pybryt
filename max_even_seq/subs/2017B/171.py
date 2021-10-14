def max_even_seq(n):
    m=str(n)
    s="" #the idea is explained below.
    for i in m:
	    if (int(i))%2==0:
		    s="y"+s
	    else:
		    s=" "+s
    k=s.split()
    v=max(len(w) for w in k)
    return(v)


