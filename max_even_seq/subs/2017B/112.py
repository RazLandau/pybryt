def max_even_seq(n):
    cnt = 0
    seq = [0]
    if n == 0:
        return 1 # 0 has one sequence
    while n>0:
        if n%2 == 0:
            cnt = cnt+1
        else: # if even sequence finishes, record the counter and nullify
            seq.append(cnt)
            cnt = 0
        n = n//10
    if n ==0:
        seq.append(cnt)
    seq.sort() # to get the maximal element of the list, sort it and return the last one
    return seq[-1]
    





