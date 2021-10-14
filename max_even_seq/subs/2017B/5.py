def max_even_seq(n):
    alllen = [0]
    m=0
    while n>0:
        if n%2 == 0:
            m += 1
            n = n//10
        elif n%2 !=0:
            alllen.append (m)
            n = n//10
            m=0
    if n == 0:
        alllen.append (m)
        a = max (alllen)
        return a
        





