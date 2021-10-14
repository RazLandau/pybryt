def max_even_seq(n):
    if(n<=9 and n%2==0):
        return 1
    elif(n<=9 and n%2!=0):
        return 0
    else:    
        check_list=[]
        counter=0
        while n>9:
            if((n%10)%2==0):
                counter = counter+1
            elif((n%10)%2!=0):
                counter=0
            n=n//10   
            check_list.append(counter)    
        length=len(check_list)
        if(check_list[length-1]==0 and n%2==0):
            check_list.append(1)
        elif(check_list[length-1]!=0 and n%2==0):
            check_list.append(check_list[length-1]+1)
    
        return(max(check_list))
        
                


    



