def max_even_seq(n):
    cnt=0
    sofi=0
    for i in str(n):
        if int(i)%2==0:
            cnt=cnt+1
            if sofi<cnt:
                sofi=cnt
        else:
            cnt=0
    return(sofi)
    





