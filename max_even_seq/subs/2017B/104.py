def max_even_seq(n):
    maxseq=0
    cnt=0
    for i in str(n):
        if int(i)%2==0:
            cnt+=1
            if cnt>maxseq:
                maxseq=cnt
        else:
            cnt=0
    return maxseq
            
    




