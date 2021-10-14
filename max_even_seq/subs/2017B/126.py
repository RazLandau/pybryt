def max_even_seq(n):
    cnt = 0
    cnt_max = 0
    ns = str(n)
    for i in ns:
        if int(i)%2 == 0:
            cnt = cnt + 1
            if cnt > cnt_max:
                cnt_max = cnt
        else:
            cnt = 0
    return (cnt_max)

