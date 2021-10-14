def max_even_seq(n):
    seq=0
    count=0
    a=str(n)
    for i in a:
        if int(i)%2==0:
            count=count+1
        else: 
            count=0
        if seq<count:
            seq=count
    return(seq)





