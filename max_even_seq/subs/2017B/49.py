def max_even_seq(n):

    maxCount = 0
    currentCount = 0
    
    for c in str(n):
        if int(c) % 2 == 0:
            currentCount += 1
        else:
            if currentCount > maxCount:
                maxCount = currentCount
            currentCount = 0
            

    if currentCount > maxCount:
        maxCount = currentCount

    return maxCount




