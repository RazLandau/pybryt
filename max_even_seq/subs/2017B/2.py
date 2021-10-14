def max_even_seq(n):
    #pass #replace with your implementation
    strnum=str(n)
    count=0
    maxcount=0
    for i in range(len(strnum)):
        if (int(strnum[i]))%2==0:
            count+=1
        else:
            if count>maxcount:
                maxcount=count
            count=0
    if count>maxcount:
                maxcount=count
    return maxcount



