def max_even_seq(n):
    cnt=0
    maxcnt=0
    while n > 0:
        res = n % 10
        n = n // 10
        if res%2==0:
            cnt+=1
        else:
            maxcnt=max(cnt,maxcnt)
            cnt=0
    return maxcnt



