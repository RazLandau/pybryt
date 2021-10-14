def max_even_seq(n):
    cnt=0
    max=0
    snum = str(n) 
    for digit in snum:
        if int(digit)%2 == 0:
            cnt = cnt+1
        else:
            cnt=0
        if cnt>max:
            max=cnt
    return (max)





