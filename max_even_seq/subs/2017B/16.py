def max_even_seq(n):
    if n==0 :
        return (1)
    else:
        b = n%10
        c = 0
        a = 0
        while n!=0:
            if b%2==0 :
                c=c+1
                n=n//10
                b=n%10
                if c>a :
                    a=c
                else :
                    pass
            else :
                c = 0
                n=n//10
                b=n%10
        return (a)


