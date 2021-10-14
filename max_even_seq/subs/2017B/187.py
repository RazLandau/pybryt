def max_even_seq(n):
    sn=str(n)
    max0=0
    max1=0
    for dig in sn:
        idig=int(dig)
        if(idig%2==0):
            max1+=1   
        if(idig%2==1):
            if(max1>max0):
                max0=max1
                max1=0
    max1=max0
    return max1
    





