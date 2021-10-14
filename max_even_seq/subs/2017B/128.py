def max_even_seq(n):
    string_n = str(n)
    max_even = 0 #"local" maximum lenght of evens
    max_max_even = 0 #"global" maximum lenght of evens
    cnt_even = 0
    for digit in string_n:
        if(int(digit)%2==0):
            cnt_even+=1
        else:
            max_even = cnt_even
            cnt_even = 0
        if(max_even > max_max_even):
            max_max_even = max_even
    return max_max_even




