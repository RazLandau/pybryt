def max_even_seq(n):   
    if n == 0:
        return 1

    max_len = 0
    count = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            count += 1
        elif count != 0:
            max_len = max([max_len, count])
            count = 0
        n //= 10

    return max_len





