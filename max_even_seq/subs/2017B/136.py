def max_even_seq(n):
    pass #replace with your implementation
    count_high=0
    count=0
    n=str(n)
    for i in range(0,len(n)):
        if ((int(n[i]))%2==0):
            count+=1
        else:
            if(count_high<count):
                count_high=count  
            count=0
    if(count_high<count):
        count_high=count
    return count_high 
   

