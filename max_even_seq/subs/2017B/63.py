def max_even_seq(n):
    pass #replace with your implementation
    fnl=0
    cnt=0
    n=str(n)
    list(n)
    for i in range(len(n)):
        if int(n[i])%2==0:
            cnt=cnt+1
        else:
            if cnt>fnl:
                fnl=cnt
            cnt=0
    if cnt>fnl:
        fnl=cnt
    return(fnl)




