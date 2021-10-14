def max_even_seq(n):
    cnt=0
    maxCnt=0
    if(n==0):
        return 1
    else:
        while(n>0):
            if((n%10)%2==0):
                cnt=cnt+1
            else:
                cnt=0
            n=n//10
            if(cnt>maxCnt):
                maxCnt=cnt
    return maxCnt






