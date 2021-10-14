def max_even_seq(n):

    strn = str(n)
    cnt = 0
    cmpr = 0
    for digit in strn:
        if int(digit)%2 == 0:
            cnt +=1
        else:
            cmpr = max(cnt, cmpr)
            cnt = 0
    cmpr = max(cnt, cmpr)
    return cmpr


