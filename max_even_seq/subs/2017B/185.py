def max_even_seq(n):   
    en = str(n)
    evens = ""
    for x in en:
        if int(x)%2 ==0:
            evens += x
        else:
            evens += " "
    listEvens = evens.split()
    m = 0
    for i in range(len(listEvens)):
        m = max(len(listEvens[i]), m) 
        
    return(m)




