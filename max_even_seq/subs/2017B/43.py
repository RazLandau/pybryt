def max_even_seq(n):
    if n==0:
        return 1
    num=n
    seq=0
    max=0
    b=False #True if the last number checked was even
    while num>0:
        if not(b):
            if (num%10)%2==0:
                seq=1
                b=True
        else:
            if (num%10)%2==0:
                seq=seq+1
                if seq>max:
                    max=seq
            else:
                    seq=0
                    b=False
        num=num//10
    return max

