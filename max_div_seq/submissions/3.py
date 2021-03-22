def max_div_seq(n, k):
    maxi=0
    c=0
    lst=list(str(n))
    for i in range(len(lst)):
        if int(lst[i])%k==0:
            c+=1
        else:
            if c>maxi:
                maxi=c
            c=0
    if c>maxi:
        maxi=c
    return maxi