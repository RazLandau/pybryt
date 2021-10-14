def max_even_seq(n):
    max_cnt=0
    if n==0:
        return 1
    while n>0:
        cnt=0
        while ((n%10)%2==0)&(n>0):
            cnt=cnt+1
            n=n//10
        if cnt>max_cnt:
            max_cnt=cnt
        n=n//10
    return (max_cnt)

