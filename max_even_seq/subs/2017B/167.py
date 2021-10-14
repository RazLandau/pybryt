def max_even_seq(n):
    maxEven = 0
    count = 0
    if n==0:
        maxEven=1
    while n>0:
        if n%10%2==0:
            count=count+1
            if maxEven<count:
                maxEven=count
        if n%10%2==1:
            count=0
        n=n//10
    return(maxEven)

