def max_even_seq(n):
    maxseq=0
    cnt=0
    for dig in str(n):
        if int(dig)%2==0:
            cnt+=1
        else:
            if cnt>maxseq:
                maxseq=cnt
            cnt=0
    if cnt>maxseq:
        maxseq=cnt
    return maxseq


