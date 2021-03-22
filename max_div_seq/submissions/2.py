def max_div_seq(n,k):
    str_n = str(n)
    max_div = []
    i = 0
    for num in str_n:
        if int(num) % k == 0:
            i += 1
        else:
            max_div.append(i)
            i = 0
    max_div.append(i)
    return (max(max_div))