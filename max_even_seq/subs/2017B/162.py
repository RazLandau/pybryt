def max_even_seq(n):
    max_seq=0
    countCurrSeq=0
    while n>0:
        if (n%10)%2==0:
            countCurrSeq+=1
            if countCurrSeq>max_seq:
                max_seq=countCurrSeq
        else:
            countCurrSeq=0
        n //= 10
    return max_seq


