def max_even_seq(n):
    strike = 0
    basket=[]
    for i in str(n):
        if int(i)%2==0:
            strike+=1
            basket += [strike]
        else:
            strike = 0
    basket.sort()
    basket.reverse()
    return (basket[0])
