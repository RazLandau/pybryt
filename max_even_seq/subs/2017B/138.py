def max_even_seq(n):
    if n<0:
        print("n must be 0 or larger")
        return
    elif type(n)!=int:
        print("n must be an integer")
        return
    else:
       stringed = str(n)
       countr = 0
       current= 0
       for char in stringed:
           if int(char)%2==0:
               current+=1
           else:
                if countr > current:
                    current=0
                else:
                    countr=current
                    current=0
       if countr < current:
            countr = current
    return(countr)



