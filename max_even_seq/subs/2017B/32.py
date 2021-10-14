def max_even_seq(n):
    snum = str(n)
    max_seq = 0
    cnt = 0

    for digit in snum:
        if int(digit) % 2 == 0:
            cnt += 1
        else:
            max_seq = max(max_seq,cnt)
            cnt = 0

    return max(max_seq,cnt)


