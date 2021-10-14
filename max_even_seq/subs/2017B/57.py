def max_even_seq(n):
    if n>=0:
        lst=[]
        cnt=0
        ns=str(n)
        for num in ns:
            n_m=int(num)
            if n_m%2==0:
                cnt+=1
                lst.append(cnt)
            else:
                cnt=0
                lst.append(cnt)
        M=max(lst)
    return M




