def max_even_seq(n):
    pass #replace with your implementation
    if n==0:
        return 1
    crntCnt = 0
    maxCnt = 0
    while n!=0:
        if int(n) % 2 == 0:
            crntCnt += 1
        else:
            crntCnt = 0
        if crntCnt > maxCnt:
            maxCnt = crntCnt
        n //= 10
    return maxCnt

