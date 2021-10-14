def max_even_seq(n):
    nfix = int("1"+str(n)+"1")
    cnt = 0
    max = 0
    mylist = [int(i) for i in str(nfix)]
    for item in mylist:
        if item%2 == 0:
            cnt += 1
        else:
            if max < cnt:
                max = cnt
            cnt = 0
    return max





