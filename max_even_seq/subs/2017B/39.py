def max_even_seq(n):
    count = 0;
    ans = 0;
    while n != 0:
        if (n%10)%2 == 0:
            count += 1
            if ans < count:
                ans = count
        else:
            count = 0
        n = n//10
    return(ans)

