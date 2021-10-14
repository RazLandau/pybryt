def max_even_seq(num):
    num_digits = [int(x) for x in list(str(num))]
    even_digits_sequance = [0]
    index = 0
    for i in num_digits:
        if i % 2 == 0:
            even_digits_sequance[index] += 1
        else:
            index += 1
            even_digits_sequance.append(0)
    return max(even_digits_sequance)

