def max_even_seq(n):
    maximum = 0
    temp = 0
    for i in range(len(str(n))):
        if (n%10)%2 == 0:
            temp += 1
        else:
            temp = 0
        if maximum < temp:
            maximum = temp      
        n = n//10
    return maximum





