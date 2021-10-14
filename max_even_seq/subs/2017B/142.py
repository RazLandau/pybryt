def max_even_seq(n):
    maxEvenLength=0
    currentLen=0
    for x in str(n):
        if(int(x)%2==0):
            currentLen+=1
        else:
            currentLen=0
        if(currentLen>maxEvenLength):
            maxEvenLength=currentLen
    return maxEvenLength





