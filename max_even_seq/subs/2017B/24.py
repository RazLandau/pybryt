def max_even_seq(n):
    if (type(n)!=int): return print("n must be integer")
    num = str(n)
    count=0
    max_even=0
    for i in num:
        if(int(i)%2==0):
            count += 1 # i is even, count goes 1 up
        else:
            max_even = max(count,max_even) # max_even is not the max sequence
            count = 0 #reset the count
    max_even = max(count,max_even)
    return max_even

       

