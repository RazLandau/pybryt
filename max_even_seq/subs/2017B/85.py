def max_even_seq(n):
    cnt=0
    r=0
    strn=str(n)
    for digit in strn:
        num=int(digit)
        if num%2==0:
            # cnt=cnt+1
            # r=max(cnt,r)
        else:
            cnt=0
    return(r)


