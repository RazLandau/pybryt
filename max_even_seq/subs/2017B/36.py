def max_even_seq(n):
    pass 
    s = str(n)
    bigc = 0
    tempc = 0
    for i in range (1,len(s)+1):
        if int(s[i-1])%2 == 0:
            tempc = tempc + 1
        else:
            tempc = 0
        if bigc < tempc:
            bigc = tempc
    return bigc

