def max_even_seq(n):
    pass #replace with your implementation
    max1 = 0
    count = 0
    for digit in str(n):
        
        if int(digit) % 2 == 0:
            count += 1
        else:
            count = 0
        if count > max1:
            max1 = count
         
    return max1



