def max_even_seq(n):
    num=n
    cur_cnt=0
    max_cnt=0
    if num==0:
        max_cnt=1
    while num>0:
        if (num%10)%2==0:
            cur_cnt+=1
            if cur_cnt>max_cnt:
                max_cnt=cur_cnt
            num//=10
        else:
            if cur_cnt>max_cnt:
                max_cnt=cur_cnt
            cur_cnt=0
            num//=10
    return max_cnt



