def max_even_seq(n):
    Num=0
    count=0
    while n>0:
        if (n%10)%2==0:
            count=count+1
            if count>Num:
                Num=count
        else:
            count=0
        n=n//10
    return(Num)


