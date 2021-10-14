def max_even_seq(n):
    evenseq = []
    d = 0
    while n>0:
        while n%2 == 0 and n>0:
            d += 1
            n = n//10
        evenseq.append(d)
        d = 0
        n = n//10
    return max(evenseq)

    



    
