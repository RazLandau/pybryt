def max_even_seq(n):
    seq = 0
    maxx = 0
    for i in str(n):
        if (int(i) % 2 == 0):
            seq += 1
        else:
            if (seq > maxx):
                maxx = seq
            seq = 0
    if (seq > maxx):
        return seq
    return maxx





