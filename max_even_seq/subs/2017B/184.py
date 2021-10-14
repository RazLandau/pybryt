def max_even_seq(n):
    sn = str(n)
    max_seq = 0
    for index in range(len(sn)):
        seq_cnt = 0
        seq_in = index
        endSeq = False
        while seq_in in range(index, len(sn)) and not endSeq:
            if int(sn[seq_in]) % 2 == 0:
                seq_cnt += 1
                seq_in += 1
            else:
                endSeq = True
                
        if seq_cnt > max_seq:
            max_seq = seq_cnt
    return max_seq





