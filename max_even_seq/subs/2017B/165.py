def max_even_seq(n):
    pass #replace with your implementation
    num=str(n)
    lst1=[]
    lst2=[]
    lst_even=[]
    lst_len=[]
    for digit in num:
        lst1.append(digit)
    l=len(lst1)
    for i in range(l):
        for j in range(l):
            lst2.append(lst1[i:j+1])
    def even_lst(lstn):
        for x in lstn:
            if all(int(x)%2==0 for x in lsti)==True:
                return True
            else:
                return False
    for lsti in lst2:
        if even_lst(lsti)== True:
            lst_even.append(lsti) 
    for lstj in lst_even:
        lst_len.append(len(lstj))
    if len(lst_len)==0:
        max_even=0
    else:
        max_even=max(lst_len)
    return(max_even)







