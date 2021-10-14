def max_even_seq(n):
   pt=str(n)
   pt=pt[::-1]
   n=int(pt)
   cnt=0
   max1=0
   for i in pt:
    i=int(i)
    if (i%2==0):
        cnt=cnt+1
        if (cnt>max1):
            max1=cnt
    elif(i%2!=0):
        cnt=0
   return (max1)
        




