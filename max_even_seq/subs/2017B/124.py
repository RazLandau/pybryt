def max_even_seq(n):
    cnt=0
    mid_cnt=0   
    for i in str(n):
        if (n%10)%2==0:
            mid_cnt+=1
            if mid_cnt>cnt:
                cnt=mid_cnt
            n=n//10
        else:
            mid_cnt=0
            n=n//10
    return(cnt)





