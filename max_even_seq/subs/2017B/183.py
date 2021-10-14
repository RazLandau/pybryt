def max_even_seq(n):
    res=0
    cnt=0
    n=abs(n)
    num=str(n)
    for char in num:
        if int(char)%2==0:
            cnt = cnt+1
        else:
            if cnt > res:
                res=cnt
            cnt = 0
    if cnt > res:
        res = cnt
    return res





