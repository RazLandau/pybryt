def max_even_seq(n):
        res=0
        max1 = 0
        num =str(n)
        for i in num:
                if int(i) %2 ==0:
                    res+= 1
                    max1 = max(res,max1)
                    
                else:
                    num=0
                    res =0

        return max1            
        



