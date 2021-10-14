def max_even_seq(n):
    count = 0
    res = 0
    if n==0:
        return('0')
    else:
        while n > 0:
            num = n % 10
            if num % 2 == 0:
                count += 1
            else:
                count = 0
            n = n//10
            res = max(res,count)
    return(res)




