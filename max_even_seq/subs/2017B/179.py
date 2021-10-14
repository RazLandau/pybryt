def max_even_seq(n):
    max_even_seq = 0
    num_even_seq = 0
    str_n = str(n)
    digit_is_even = False
    for digit in str_n:
        if int(digit) % 2 == 0:
            digit_is_even = True
            num_even_seq += 1      
        else:
            digit_is_even = False
            if num_even_seq > max_even_seq:
                max_even_seq = num_even_seq
            num_even_seq = 0
    if (digit_is_even == True):
        max_even_seq = num_even_seq
    return max_even_seq



