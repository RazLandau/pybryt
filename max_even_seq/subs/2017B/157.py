def max_even_seq(n):
    str_n = str(n)
    cur_seq = 0
    max_seq = 0
    for i in str_n:
        if (int(i) % 2) == 0:
            cur_seq += 1
            if cur_seq > max_seq:
                max_seq = cur_seq
        elif int(i) % 2 != 0:
            cur_seq = 0
    return max_seq




