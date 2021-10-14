def max_even_seq(n):
    #pass #replace with your implementation

    my_number = str(n)
    
    counter = 0
    max_counter = 0
    
    for c in my_number:
        if (int(c)%2==0):
            counter = counter + 1
        else:
            if (counter > max_counter):
                max_counter = counter
            counter = 0

    return max_counter


