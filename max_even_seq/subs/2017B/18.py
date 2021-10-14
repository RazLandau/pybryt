def max_even_seq(n):
    max_ = 0
    curr = 0
    for x in range(len(str(n))):
        digit = n%10
        if digit%2 == 0:
            curr += 1
            if curr > max_:
                max_ = curr
        else:
            curr = 0
        n = n//10
    return max_
        





