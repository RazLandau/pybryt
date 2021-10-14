def max_even_seq(n):
    n = str(n)

    lst = []
    cnt = 0
    maxc = 0
    
    for i in range(0,len(n)):
        if int(n[i])%2 !=0:
            cnt = 0
        elif int(n[i])%2 ==0:
            cnt += 1
        if maxc < cnt:
            maxc = cnt
    return maxc




