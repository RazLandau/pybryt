def max_even_seq(n):
    max = 0
    cur = 0
    for s in str(n):
        if int(s) % 2 == 0:
            cur += 1
        else:
            cur = 0
        if (cur > max):
            max = cur
    return max


