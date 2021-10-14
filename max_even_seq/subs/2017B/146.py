def max_even_seq(n):
    count=0
    ln=[]
    for i in str(n):
        if int(i)%2==0:
            count+=1
        else:
            ln.append(count)
            count=0
    if (int(str(n)[-1]))%2==0:
        ln.append(count)
    return max(ln)
        
