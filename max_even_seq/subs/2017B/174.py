def max_even_seq(n):
    cnt=0
    mx=0
    for i in str(n):
        if (int(i)%2==0):
            cnt=cnt+1
        else:
            cnt=0
        if (cnt>mx):
            mx=cnt
    return mx




