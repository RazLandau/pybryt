def max_even_seq(n):
    cnt1=0
    cnt2=0
    for i in str(n):
        if int(i) % 2 == 0:
            cnt1 += 1
            if cnt1 > cnt2:
                cnt2 = cnt1
        else :
            cnt1=0

    return cnt2

