def max_even_seq(n):
    max1=0
    cnt=0

    while n>0:
        if (n%10)%2==0:
            cnt+=1
        else:
            if cnt>max1:
                max1=cnt
            cnt=0
        n=n//10
       
    return max(cnt,max1)


