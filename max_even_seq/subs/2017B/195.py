def max_even_seq(n):
    seq = 0
    maxi = 0
    for i in str(n):
        if int(i)%2 == 0:
            seq += 1
            if seq > maxi:
                maxi = seq
        else:
            seq = 0
    return maxi
    





