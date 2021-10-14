def max_even_seq(n):
    pass odd=0
    temp=0
    op=len(str(n))
    for i in range(1,op+1):
        num=n%10
        n=n//10
        if num%2!=0:
            if temp>odd:
                odd=temp
            temp=0    
        if num%2==0:
            temp=temp+1
            if i==op and odd<temp:
                odd=temp
    return odd        


