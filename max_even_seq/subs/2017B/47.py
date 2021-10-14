def max_even_seq(n):
    cnt = 0
    max_cnt = 0
    for i in str(n):
        if int(i) % 2 == 0: cnt += 1
        else: cnt = 0
        if max_cnt < cnt: max_cnt = cnt
    return max_cnt
        
