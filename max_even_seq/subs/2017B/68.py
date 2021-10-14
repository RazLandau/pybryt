def max_even_seq(n):
    maxeven = 0
    current = 0
    for i in [int(x) for x in str(n)]:
        if i%2==0:
            current += 1
        else:
            current = 0
        if maxeven < current:
                maxeven = current
    return maxeven


