def max_even_seq(n):

    count = 0
    maxx = 0
    
    while n>0 :
        if ((n%10)%2 == 0):
            count += 1
        else:
            if maxx < count :
                maxx = count
            count = 0
        n = n//10

    if (count<maxx):   
        return(maxx)
    else:
        return(count)





