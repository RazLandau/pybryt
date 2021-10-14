def max_even_seq(n):
    nStr = str(n)
    cnt = 0
    maxEven = 0
    for dig in nStr:
        if int(dig)%2!=0:
            cnt=0
        else:
            cnt += 1
            maxEven = max(cnt, maxEven)
    return (maxEven)




