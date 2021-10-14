def max_even_seq(n):
    max=0
    cnt=0
    for dig in str(n):
        if int(dig)%2==0:
            cnt+=1
            if cnt>max:
                max=cnt
        else:
            cnt=0
    return (max)


