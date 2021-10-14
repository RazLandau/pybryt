def max_even_seq(n):
    pass #replace with your implementation
    list1 = []
    x,y,z=0,0,0
    while n>0:
        while n%2 == 0 and n !=0:
            x += 1
            n = n//10
        list1.append(x)
        x=0
        n = n//10
    for i in list1:
        if list1[z] > y :
            y=list1[z]
        z += 1
    return(y)



