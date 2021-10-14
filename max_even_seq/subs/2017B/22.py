def max_even_seq(n):

    #special inputs check:
    if (n==0):
        return 1
    elif (n<0):
        return print("Invalid input, n must belong to Natural numbers")
        
    max_seq = 0

    count = 0

    temp = -1

    #division and standard checks algorithm
    while(n > 0):

        #print("N is :", n)
        #print("Max = ", max_seq, " count = " , count, " temp = ", temp )
            
        temp = n%10
        
        if (temp % 2 == 0):
            count += 1
            if (max_seq < count):
                max_seq = count

        else:
            count = 0

        n = n//10 #reduction of n, prepeartion for the next digit

    return(max_seq)
       
