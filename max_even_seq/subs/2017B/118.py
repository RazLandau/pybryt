def max_even_seq(n):
    counter=0
    max_counter=0
    while n!=0:
        if (n%10)%2==0:
        
            counter=counter+1
            if max_counter<counter:
                max_counter=counter     
        else:
            counter=0

        n=n//10
                  

    return max_counter





