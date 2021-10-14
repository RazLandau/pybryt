def max_even_seq(n):
    max_seq = 0
    cnt = 0
    if n == 0:
        return 1
    while n>0:
        if n%2 == 0:
            cnt = cnt + 1
            if cnt > max_seq:
                max_seq = cnt
        else:
            cnt = 0
        n = n // 10
    return max_seq



