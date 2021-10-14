def max_even_seq(n):
    pass #replace with your implementation
    retNum=-1
    ##check that n is int and non-negative as needed
    if str(type(n))=="<class 'int'>":
        if n>=0:
            numStr=str(n)
            count=0
            for d in numStr:
                if int(d)%2==0:
                    count+=1
                else:
                    if count>retNum:
                        retNum=count
                    count=0
    return retNum





