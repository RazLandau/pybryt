def max_even_seq(n):
    if n==0:
        return 1
    count=0
    max_sequence=0
    while n!=0:
        if n%2==0:
            count=count+1
        else:
            max_sequence=max(max_sequence, count)
            count=0
        n=n//10
    return max_sequence




