def max_even_seq(n):
    tempEven = 0  # will be used to save the length new sequence while iterating
    longstEven = 0  # the length longest even sequence untill now
    for i in str(n):  # iterating (n) as a string
        if int(i) % 2 == 0:  # checks if the cuurent number is even
            tempEven += 1  # counts the lengh of the current seque
        elif tempEven != 0:  # if the number is odd, and tempEven is not = 0, then tempEven = 0.
            tempEven = 0
        if tempEven > longstEven:  # if a longer sequence is found, it's length is saved
            longstEven = tempEven
    return longstEven


