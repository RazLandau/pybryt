def max_even_seq(n):
    ans = 0 # the returned value, max even sequence
    cnt = 0 # counter of current even sequence
    if n == 0: # if the input is 0, then it is a single even digit
        return 1
    while n> 0:
        if (n%10)%2== 0: # if the last digit is even
            cnt = cnt+1 #add 1 to the sequence counter
        else:
            if cnt> ans: #is the current sequence is the longest
                ans = cnt #update the max counter
            cnt = 0 # the sequence has been broken, reset the counter
        n = n//10 #remove the last digit as it has been checked
       
    return max(cnt , ans) # return cnt if the max sequence is at the beggining of n

