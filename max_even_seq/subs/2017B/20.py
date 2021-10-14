def max_even_seq(n):
    i=0
    x=0
    z=0
    num = int(n)
    while num > 0:
        i = i + (num % 10)
        num = num // 10
        if i % 2 == 0:
            x+=1
            if z<x:
                z=x
        else:
            x=0
        i=0
    return(z)        
            

