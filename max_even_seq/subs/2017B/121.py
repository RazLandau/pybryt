def max_even_seq(n):
    max_even = 0
    count = 0
    for digit in str(n):
        if int(digit)%2 ==0:
            count += 1
        else:
            max_even = max(count, max_even)
            count = 0
    max_even = max(count,max_even) 
    return (max_even)

