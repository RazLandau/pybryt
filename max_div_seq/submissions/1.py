def max_div_seq2(n, k):
    cnt_chk = 0
    cnt_max = 0
    n_to_str = str(n)
    for i in n_to_str:
        if int(i) % k == 0:
            cnt_chk += 1
            cnt_max = max(cnt_chk, cnt_max)
        else:
            cnt_chk = 0

    return cnt_max