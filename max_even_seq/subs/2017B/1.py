def max_even_seq(n):
    x=0
    maxx=0
    while n>0:
        if n%2==0:
            x+=1
        else:
            maxx=max(maxx,x)
            x=0
        maxx=max(maxx,x)
        n=int(n/10)
    return(maxx)


