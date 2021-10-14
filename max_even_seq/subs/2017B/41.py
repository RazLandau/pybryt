def max_even_seq(n):
    pass #replace with your implementation
    m = n
    cnt = 0
    H=[]
    while m>0:
         if (m%10)%2 == 0:
             cnt+=1
         else:
            H.append(cnt)
            cnt=0
         m = m//10
    return max(H)
   


