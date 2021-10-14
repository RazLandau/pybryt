def max_even_seq(n):
    long_seq=0
    max_seq=[]
    for i in str(n):
      if int(i)%2 ==0:
        long_seq=long_seq+1
        max_seq.append(long_seq)  
      else:
        long_seq=0
        max_seq.append(long_seq)  
     
    return (max(max_seq))





