def max_even_seq(n):
    max_len = 0
    while n > 0:
        if n%2 == 0:
            cnt += 1
            n = n//10
            if cnt>max_len:
                max_len=cnt
        else:
            cnt = 0
            n = n//10
    return(max_len)




