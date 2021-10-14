def max_even_seq(n):
    
    temp = ""
    l1 = []
    x=str(n)
    for i in x:
        y =int(i)
        if y%2== 0: 
            temp= temp +i
       
        if y%2 != 0:
            temp = ""
        
        biger = temp
        l1.append(biger)
    m= max(l1, key=len)
    a= int(len(m))
   
    return(a)


