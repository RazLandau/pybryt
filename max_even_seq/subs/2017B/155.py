def max_even_seq(n):
    n = str(n)
    maxSeq = 0
    currentSeq = 0
    for dig in n:
        if int(dig) % 2 == 0:
            currentSeq += 1
            maxSeq = max (maxSeq, currentSeq)
        else:
            currentSeq = 0
    return maxSeq





