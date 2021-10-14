def max_even_seq(n):
    counter = 0
    maxi = 0
    for i in str(n):
        if int(i)%2 == 0:
            counter = counter + 1
            if maxi < counter:
                maxi = counter
        else:
            counter = 0
    return(maxi)

