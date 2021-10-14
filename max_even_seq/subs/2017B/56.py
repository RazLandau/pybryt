def max_even_seq(n):
    maxseq = 0
    length = 0
    for digit in str(n):
        if (int(digit)%2 == 0):
            length += 1
        else:
            length = 0
        if (length > maxseq):
            maxseq = length
    return maxseq




