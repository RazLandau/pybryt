def max_even_seq(n):
    if n==0:
        print(1)
    else:
        list=[0]
        while n>0:
            if((n%10)%2)==0:
                counter=0
                while((n%10)%2)==0 and n>0:
                    counter+=1
                    n//=10
                list.append(counter)
            n//=10
        return (max(list))




