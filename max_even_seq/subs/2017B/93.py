def max_even_seq(n):
    x = n
    mlst = [0]
    count = 0
    for i in str(n):
        if int(i)%2 == 0:
            count = count +1
        else:
            if count != 0:
                mlst.append(count)
            count = 0
    return(max(mlst))





