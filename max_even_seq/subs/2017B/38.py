def max_even_seq(n):
    sequences=[]
    count=0
    for d in str(n):        
        if int(d)%2==0:
            count+=1
        else:
            sequences.append(count)
            count=0
        sequences.append(count)
    return max(sequences)



