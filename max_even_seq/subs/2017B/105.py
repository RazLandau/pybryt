def max_even_seq(n):
    tempseq=0 #temporary sequence counter
    finalseq=0
    for deg in str(n):
        if int(deg)%2==0:
            tempseq=tempseq+1
        else:
            if tempseq>finalseq:
                finalseq=tempseq
                tempseq=0
            else:
                tempseq=0
    if tempseq>finalseq:
        return tempseq
    else:
        return finalseq





