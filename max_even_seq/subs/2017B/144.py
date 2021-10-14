def max_even_seq(n):
    cnt = 0
    num = n
    max_seq = 0
    while num>0:
        if num%2==0:
            cnt+=1
        if cnt > max_seq:
            max_seq = cnt
        if num%2 != 0:
            cnt = 0
        num = num//10
    return max_seq





