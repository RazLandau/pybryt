def max_even_seq(n):
    bank = 0
    count = 0
    for digit in str(n):
        if int(digit)%2 == 0:
            count += 1
        else:
            if count>bank:
                bank = count
                count = 0
            else:
                count = 0
    return(bank)


