def max_even_seq(n):
    count = 0
    max_count=0
    for i in str(n):
        if (int(i)%2!=0 and count>0):
            if(count>max_count):
                max_count=count
            count=0
        elif int(i)%2==0:
            count=count+1
    if(count>max_count):
        max_count=count
    return max_count
