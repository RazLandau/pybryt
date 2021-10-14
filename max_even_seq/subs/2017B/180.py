def max_even_seq(n):
    cnt=0
    maxim=0
    string=str(n)
    lasteven= False
    for char in string:
        if (int(char)%2==0):
            lasteven=True
            cnt+=1
        else:
            lasteven=False
            maxim=max(maxim,cnt)
            cnt=0
    return max(maxim,cnt)





