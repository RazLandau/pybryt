def max_even_seq(n):
    max_even = 0
    temp=0
    while n>0:
        if(n%10)%2!=0:
            temp=0
        else:
            temp = temp+1
            if temp>max_even:
                max_even=temp
        n=n//10
    return(max_even)
