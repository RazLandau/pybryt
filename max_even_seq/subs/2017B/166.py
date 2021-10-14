def max_even_seq(n):
    MaxEven=0
    TempMax=0
    int_num=int(n)
    if (int_num==0):
        MaxEven=1
    else:
        while (int_num!=0):
            while (((int_num%10)%2)==0 and int_num!=0): 
                TempMax+=1
                int_num//=10
            if MaxEven<TempMax :
                MaxEven=TempMax    
            TempMax=0
            int_num//=10
            
    return(MaxEven)



