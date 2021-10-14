def max_even_seq(n):
    cnt=0
    listt=[0]
    while n>0:
        if n%2==0:
            cnt=cnt+1
            n=n//10
            list.append(listt, cnt)
        else:
            cnt=0
            n=n//10


    return (max(set(listt)))




