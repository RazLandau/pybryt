def max_even_seq(n):
    max_res = 0
    cnt = 0
    while n > 0:
        dig = n % 10
        if dig % 2 == 0:
            cnt = cnt + 1
            if cnt > max_res:
                max_res = cnt
        else:
            if cnt > max_res:
                max_res = cnt
            cnt = 0
        n = n // 10
    return max_res

