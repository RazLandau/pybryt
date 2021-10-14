def max_even_seq(n):
    i=0
    a=[]
    for digit in str(n):
        if int(digit)%2==0:
            i = i+1
        else:
            a.append(i)
            i=0
    a.append(i)
    return(max(a))





