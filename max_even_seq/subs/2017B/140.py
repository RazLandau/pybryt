def max_even_seq(n):
    cnt = 0
    lst = []
    for i in str(n):
        if int(i)%2 == 0:
            cnt = cnt + 1
            lst.append(cnt)
        else:
            cnt = cnt*0
            lst.append(cnt)

    return max(lst)


