def max_even_seq(n):
    totalMax=0
    tempMax=0
    if n==0:
        return 1
    else:
        while n!=0:
            if n%2==0:
                tempMax+=1
            else:
                tempMax=0
            if tempMax>totalMax:
                totalMax=tempMax
            n//=10
    return totalMax

