def max_even_seq(n):
  #  pass #replace with your implementation
 newnum=n
 max=0
 count=0
 while(newnum!=0):
     if newnum%2==0:
         count=count+1
         if max<count:
             max=count
     else:
         count=0
     newnum//=10
 return max

