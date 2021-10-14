def max_even_seq(n):
    count=0
    maxx=0
    while n>0:
        if n%2==0:
            count+=1
            n=n//10
        else:
            if maxx<count:
                maxx=count
            count=0
            n=n//10
    return maxx         






