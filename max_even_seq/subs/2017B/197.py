def max_even_seq(n):
    if(n == 0):
        return 1
    maxLength = 0
    counter = 0
    while (n > 0):
        if (n % 2 == 0):  # if n is even that means the last charcter is even.
            counter = counter + 1
            if maxLength < counter:
                maxLength = counter
        else:
            counter = 0
        n = n // 10  # Removing the last digit
    return maxLength


