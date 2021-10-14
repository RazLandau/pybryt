def max_even_seq(n):
    maxseq=0
    if n==0:
        maxseq=1
    else:
        while n>0: 
            cnt=0 # temporary counter for number of even consecutive digits
            while (n%10)%2==0 and n>0: # increase count as long as the the last digit is even
                cnt=cnt+1
                n=n//10 # remove last digit
            if cnt > maxseq: # check if the temporary even number sequence is longer than the current max
                maxseq=cnt 
            n=n//10
    return maxseq



