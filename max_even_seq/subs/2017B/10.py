def max_even_seq(n):

    num= str(n)
    count = 0
    maxx = 0
    lst = []
    for item in num:    
        if int(item)%2 ==0:
            count = count + 1
        else:
            lst = lst+ [count]
            count = 0
    lst= lst + [count]

    for x in lst:
        if x > maxx:
            maxx = x
    return maxx

