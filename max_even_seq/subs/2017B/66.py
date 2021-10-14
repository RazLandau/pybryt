def max_even_seq(n):
    max_even=0
    counting_even=0
    if n==0:
        max_even=1
    while n>0:
        if (n%10)%2==0:
            counting_even += 1
        else:
            counting_even=0
        if counting_even>max_even:
            max_even=counting_even
        n=n//10
    return max_even





