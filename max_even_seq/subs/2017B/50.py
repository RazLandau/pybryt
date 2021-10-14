def max_even_seq(n):

    import math


    cnt = 0
    tmp = 0
    while n > 0 :
        l = n % 10
        if l % 2 == 0:
            tmp = tmp + 1
            if tmp > cnt:
                cnt = tmp
        else:
            tmp = 0
        n = n / 10
        n = math.floor(n)
    return cnt





