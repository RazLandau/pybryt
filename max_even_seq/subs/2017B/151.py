def max_even_seq(n):
    evens = '24680'
    maxseq = 0
    curseq = 0
    for s in str(n):
        if s in evens:
            curseq += 1
        else:
            maxseq = max(curseq, maxseq)
            curseq = 0
    return max(curseq, maxseq)
            



