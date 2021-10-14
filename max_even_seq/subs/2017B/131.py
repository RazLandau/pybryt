def max_even_seq(n):
    zugi=["0","2","4","6","8"]
    
    count=0
    rezef=[]
    for i in str(n):
        if i in zugi:
            count+=1
        else:
            rezef.append(count)
            count=0
    return max(rezef)
    


