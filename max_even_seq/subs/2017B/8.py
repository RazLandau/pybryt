def max_even_seq(n):
    a=0
    am=0
    n=str(n)
    for i in (n):
        if int(i)%2==0:
            a+=1
        else:
            if am<a:
                am=a
            a=0
    return am

