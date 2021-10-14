def max_even_seq(n):
    maxCounter = 0
    counter = 0
    for digit in str(n):
        isEven = int(digit) % 2 == 0
        counter = (counter * isEven) + isEven * isEven
        maxCounter = max(maxCounter, counter)
    return maxCounter


