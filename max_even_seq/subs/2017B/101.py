def max_even_seq(n):
    new=""
    result=""
    for k in str(n):
        if int(k)%2==0:
            new=new+str(k)
        else:
            new=new+" "
    even_list= new.split(' ')
    while "" in even_list:
        even_list.remove("")
    if len(even_list)!=0:
        for number in even_list:
            if len(str(number))>len(str(result)):
                result= len(number)
    else:
          result=0
        
    return(result)    

                       
        


