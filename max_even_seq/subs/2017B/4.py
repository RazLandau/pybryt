def max_even_seq(n):
    even_dig = 0
    maximum = 0
    for i in str(n):
        if int(i)%2 == 0:
            even_dig = even_dig + 1
            if even_dig > maximum:
                maximum = even_dig
        else:
            even_dig = 0
    return maximum


        
            
            




