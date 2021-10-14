def max_even_seq(n):
    max_seq=[0]
    counter=0
    while n>0:
        if (((n%10)%2)==0):
            counter+=1
        else:
            max_seq.append(counter)
            counter=0
        n//=10
    max_seq.append(counter)
    return max(max_seq)





