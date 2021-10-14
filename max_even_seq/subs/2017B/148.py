def max_even_seq(n):
    a = str (n)
    b = len (a)
    max = 0
    temp = 0
    for i in range (b):
        temp = 0
    
        while i<b and int(a[i])%2 ==0  :
            temp = temp + 1
            i = i+1
        if temp > max:
            max = temp

    return max
        





