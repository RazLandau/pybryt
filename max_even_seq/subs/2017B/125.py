def max_even_seq(n):
    count = 0
    max_count = 0
    for char in str(n):
        if int(char) % 2 == 0:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count      
            



