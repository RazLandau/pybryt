def max_even_seq(n):
    count=0
    max_count=0
    num=str(n)
    for c in num:
        if int(c)%2==0:
            count+=1
        else:
            if(count>=max_count):
                max_count=count
            count=0
    print (max_count)          
             



    
