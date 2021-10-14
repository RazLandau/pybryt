def max_even_seq(n):
    snum = str(n)
    val = 0
    cnt = 0
    for i in snum:
        num_i = int(i)
        if num_i %2 == 0 :
            cnt = cnt+1
        else:
            cnt = 0
        if cnt>val :
            val = cnt
        else:
            val = val
    return val




