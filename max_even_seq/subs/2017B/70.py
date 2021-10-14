def max_even_seq(n):
       maxE=0
       temp=0
       while n>0:
           if n%2==0:
                  temp=temp+1
                  if temp>maxE:
                         maxE=temp
           else:
                  temp=0
           n=n//10       
       return maxE              

