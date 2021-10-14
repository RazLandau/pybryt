def max_even_seq(n):
    pass 
    cnt = 0
    m=0
    while n>0:
        if (n%10)%2==0:
            cnt = cnt+1
        else:
           cnt = 0
        if cnt>m:
            m=cnt
        n=n//10
    return (m)
    
