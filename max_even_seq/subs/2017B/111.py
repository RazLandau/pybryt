def max_even_seq(n):
    count = 0
    max_count = 0

    for i in str(n):
        if int(i) % 2 == 0:
            count += 1
        else:
            max_count = count
            count = 0

    return max(max_count, count)


