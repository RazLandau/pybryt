def max_even_seq(n):
    evencounter = 0
    maxeven = 0
    while(n>0):
        num = n%10
        if num%2==0:
            evencounter = evencounter + 1
        else:
            if evencounter>maxeven:
                maxeven = evencounter
            evencounter = 0
        n = n//10
    return(maxeven)
    
                
        
        
    
    





