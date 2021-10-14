def max_even_seq(n):
    max_seq = 0
    even_digits = 0
    if n == 0:
        return 1
    while n >0:
        if n%2 == 0:
            even_digits = even_digits + 1 #adding 1 to count if last character is even
            if even_digits > max_seq:
                max_seq = even_digits
        else:
            even_digits = 0 #resetting if last character is odd
        n = n // 10 #next character
    return max_seq
    
            
            
            






