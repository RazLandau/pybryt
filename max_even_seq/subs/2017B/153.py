def max_even_seq(n):
    # convert n to string
    sn = str(n)
    # create counters
    max_count = 0
    temp_count = 0
    # iterate through digits
    for d in sn:
        if (int(d) % 2) == 0:
            temp_count += 1
        else:
            max_count = max(max_count, temp_count)
            temp_count = 0
    return max_count




