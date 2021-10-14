def max_even_seq(n):
    pass #replace with your implementation
    fcnt = 0
    cnt = 0
    while n>0:
        le = n%10
        if(cnt>fcnt):
            fcnt=cnt
        if(le%2 == 0):
            cnt+=1
        else:
            cnt = 0
        n=n//10
    return fcnt




