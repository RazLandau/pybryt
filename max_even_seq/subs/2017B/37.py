def max_even_seq(n):
    length = 0
    templength = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            templength = templength + 1
            if templength > length:
                length = templength
        else:
            templength = 0
    print(length)
        





