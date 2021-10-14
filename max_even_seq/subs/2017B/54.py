def max_even_seq(n):
    pass #replace with your implementation
    num = 0
    max_s = []
    for i in str(n):
        if (int(i)%2==0):
            num = num + 1
        else:
            max_s.append(num)
            num = 0
    if (int(str(n)[len(str(n))-1]))%2 == 0:
        max_s.append(num)
    return (max(max_s))




