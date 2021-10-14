def max_even_seq(n):
    max1=0
    cnt=0
    if(n==0):
        print ("1")
    else:
        while(n>0):
            if(n%2==0):
                cnt+=1
            else:
                if(cnt>max1):
                    max1=cnt
                cnt=0
            n//=10
        if(cnt>max1):
            max1=cnt
        return max1





