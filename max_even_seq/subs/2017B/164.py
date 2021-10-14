def max_even_seq(n):
    tmax= 0
    seq = 0 
    for i in str(n):
        if int(i)%2==0 and str(n)[-1]==i:
            seq = seq + 1
            if seq > tmax:
                tmax = seq
        elif int(i)%2==0:
            seq = seq + 1
        else:
            if seq > tmax:
                tmax = seq
            else:
               pass
            seq = 0
    return(tmax)


