def max_even_seq(n):
    c=0
    m=0
    while n>0:
        if (n%10)%2==0:
            c+=1
        else:
            if c>m:
                m=c
            c=0
        n//=10
    if c>m:
        m=c
    return(m)

