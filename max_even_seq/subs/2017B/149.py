def max_even_seq(n):
    cnt=0
    maxcnt=0
    for i in str(n):
        if int(i)%2==0:
            cnt+=1
            if cnt>maxcnt:
                maxcnt = cnt
        else:
            cnt=0
    return (maxcnt)


