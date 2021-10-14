def max_even_seq(n):
    cnt = 0
    h_cnt = cnt
    d = str(n)
    for digit in d:
        if int(digit) % 2 == 0:
            cnt = cnt + 1
        elif cnt >= h_cnt :
            h_cnt = cnt
            cnt = 0
        else:
            cnt = 0
    int_cnt = int(h_cnt)
    return (int_cnt)
    print (int_cnt)





