def max_even_seq(n):
    num_even=0
    num_evenmax=0

    while n>0:
        if n%2==0:
            num_even+=1
            if  num_evenmax<num_even:
                num_evenmax=num_even
        else:
            num_even=0
        n=n//10
    
    return(num_evenmax)



