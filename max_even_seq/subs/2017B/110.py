def max_even_seq(n):
    cur_seq=0
    max_seq=0
    x = str(n)
    for c in x:
        i = int(c)
        if i % 2 == 0:
            cur_seq = cur_seq + 1
        else:
            max_seq = max(max_seq,cur_seq)
            cur_seq=0
    max_seq = max(max_seq, cur_seq)
    return max_seq


