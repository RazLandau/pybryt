def max_even_seq(n):
    cnt=0
    lst=[]
    strn=str(n)
    for x in strn:
        if int(x)%2==1:
            lst.insert(0,cnt)
            cnt=0
        else:
            cnt=cnt+1
            lst.insert(0,cnt)
    print(max(lst))

        
        


