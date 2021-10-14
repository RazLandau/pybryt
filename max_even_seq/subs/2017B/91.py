def max_even_seq(n):
    cnt = 0
    maxDigits = 0
    while n > 0:
        if n % 2 == 0:
            cnt += 1
            if cnt > maxDigits:
                maxDigits = cnt
        else:
            cnt = 0
        n = n // 10
    return maxDigits





