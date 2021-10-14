def max_even_seq(n):
    pass length=0
    lengthX=0
    for i in num:
        if int(i)%2==0:
            lengthX=lengthX+1
            if lengthX>length:
                length=lengthX
        else:
            lengthX=0
    print("The maximal length is", length)

