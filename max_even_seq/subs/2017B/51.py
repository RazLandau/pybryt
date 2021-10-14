def max_even_seq(n):
    n = [int(x) for x in str(n)]
    l = len(n)
    d = 0
    cnt = 0
    high = 0
    for i in range(l):
        d = l-1
        while ((n[i]%2==0) & (i != d)) :
            cnt = cnt + 1
            i = i+1
        else:
            if n[i]%2==0:
                cnt = cnt+1
        if cnt>high:
            high =cnt
        cnt = 0
    print (high)
        





