def max_even_seq(n):
    li=[]
    if n==0: return 1
    while n!=0:
        cnt=0
        while n%2==0 and n!=0:
            cnt+=1
            n=n//10
        n=n//10
        li.append(cnt)
    li.sort()
    return (li[len(li)-1])





