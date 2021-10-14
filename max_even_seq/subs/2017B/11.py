def max_even_seq(n):
    count = 0
    max_digit = 0
    lst = [int(i) for i in str(n)]
    # print(lst)
    num = int(n) % 10
    n = n // 10
    while num != 0:
        if num % 2 == 0:
            count += 1
        elif count > max_digit:
            max_digit = count
            count = 0
        num = num % 10
        n = n // 10
    if count > max_digit:
        max_digit = count
    return max_digit


