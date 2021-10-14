def max_even_seq(n):
    seqs=[]
    x=0
    place=0
    res=str(n)
    length=len(res)
    for i in res:
        place += 1
        if int(i)%2==0:
            x=x+1
        else:
            seqs.append(x)
            x=0
        if place==length:
            seqs.append(x)
    
    return (max(seqs))






