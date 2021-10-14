def max_even_seq(n):
    length = 0
    max_length = 0
    for t in str(n):
        if int(t)%2==0:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 0
    return (max_length)



