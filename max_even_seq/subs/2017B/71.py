def max_even_seq(n):
    tempDigit=0
    tempLen=0
    maxLen=0
    sequenceFlag=False

    while n>0:
        tempDigit=n%10
        if (tempDigit%2==0):
            tempLen=tempLen+1
            if sequenceFlag==False:
                sequenceFlag=True
            if tempLen>maxLen:
                maxLen=tempLen
        else:
            sequenceFlag=False
            tempLen=0
        n=n//10
    print (maxLen)

