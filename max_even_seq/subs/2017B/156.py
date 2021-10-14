def max_even_seq(n):
    max1=0
    count=0
    num=n
    flag=0
    if num==0:
        return 1
    while num >0: 
        if num<10 and num%2==0:
            return max(count+1, max1)
            
        if (num%10)%2==0: 
            count=count+1
            flag=1
        else:
            if flag==1:
                if count>max1:
                    max1=count
                count=0
                flag=0
        num=num//10
    return max1





