def max_even_seq(n):
    max_seq = 0
    counter = 0
    for i in str(n):
        i = int(i)
        if i % 2 == 0:
            counter += 1
        else:
            max_seq = max(counter, max_seq)
            counter = 0
    max_seq = max(counter, max_seq)
    return max_seq





