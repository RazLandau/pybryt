def max_even_seq(n):
    str_check = str(n)
    counter= 0
    max_counter=0
    for digit in str_check:
        if (int(digit)%2==0):
            counter +=1
        else:
            max_counter = max(counter,max_counter)
            counter=0
    return max_counter        





