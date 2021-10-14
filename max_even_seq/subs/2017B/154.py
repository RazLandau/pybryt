def max_even_seq(n):
    max_length = 0
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 == 0:
            current_length = 0
            while i < len(str(n)) and int(str(n)[i]) % 2 == 0:
                current_length += 1
                #print(current_length)
                i += 1
                #print(i)
            if current_length > max_length:
                max_length = current_length
    return max_length


