def max_even_seq(n):
    cnt = 0
    li = [0]
    if n==0:
       maximum = 1
    else:
        while n > 0:
            if n%2==0:
                cnt = cnt + 1
                n = (n//10)
            else:
                li = li + [cnt]
                cnt = 0
                n = (n//10)

        maximum = max(li)

    return maximum


