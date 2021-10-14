def max_even_seq(n):
    pass #replace with your implementation
    num = n
    maxi = 0
    maxi1 = 0
    if num>=0 and num<=9:
        if num%2==0:
            return 1
        else:
            return 0
    elif n>=10:
        lstnum = num%10
        num = num//10
        while num>0:
            if lstnum%2==0:
                while lstnum%2==0 and num>0:
                    maxi1 +=1
                    lstnum = num%10
                    num = num//10
                if lstnum%2==0:
                    maxi1 +=1
                if maxi1>maxi:
                    maxi = maxi1
                maxi1 = 0
            else:
                lstnum = num%10
                num = num//10           
        return maxi
            

