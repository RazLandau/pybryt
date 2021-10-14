def max_even_seq(n):
    cnt = 0
    max_cnt = 0
    num = str(n)
    for i in num:
        if int(i) % 2 == 0:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0
            
    return max_cnt




