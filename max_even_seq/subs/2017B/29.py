def max_even_seq(n):
    cntp=0
    while (n>0):
        cntl=0
        if((n%10)%2==0):
            while ((n>0) and ((n%10)%2==0)): #while the last digit is an evan number and the number is not 0
                cntl=cntl+1
                n=n//10
            if (cntl>cntp):
                cntp=cntl
        else:
            n=n//10
    return cntp


