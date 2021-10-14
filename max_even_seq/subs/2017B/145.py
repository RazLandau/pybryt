def max_even_seq(n):
    maxLen=0
    cnt = 0
    num=str(n)
    for dig in num:
        if int(dig)%2==0:
            cnt = cnt + 1
        else:
            if cnt>maxLen:
                maxLen = cnt
            cnt = 0
        
    return(maxLen)
         
