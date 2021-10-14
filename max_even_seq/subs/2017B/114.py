def max_even_seq(n):
    maxpint = 0
    pint = 0
    for i in str(n):
        if int(i)%2 == 0:
            pint += 1
            if maxpint < pint:
                maxpint = pint
        else:
            pint = 0
    return maxpint





