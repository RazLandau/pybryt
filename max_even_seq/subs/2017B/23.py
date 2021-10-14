def max_even_seq(num):
    snum=str(num)
    curLen=0
    maxLen=0
    for dig in snum:
        if int(dig)%2==0:
            curLen+=1
        else:
            maxLen=curLen
            curLen=0
    return max(curLen,maxLen)
