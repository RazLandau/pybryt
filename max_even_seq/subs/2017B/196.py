def max_even_seq(n):
    cnt=" "
    for x in str(n):
        if int(x)%2==0:
            cnt=cnt+"1"
        else:
            cnt=cnt+"  "
    a=str.split(cnt)
    if a==[]:
        return 0
    else:
        return (len(max(a)))
   
   
   
    





