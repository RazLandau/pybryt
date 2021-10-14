def max_even_seq(n):
    lst=[]
    cnt=0
    for i in str(n):
        if int(i)%2==0:
            cnt+=1
        else:
            lst.append(cnt)
            cnt=0
    return(max(lst))





