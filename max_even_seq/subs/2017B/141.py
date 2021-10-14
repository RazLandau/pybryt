def max_even_seq(n):
        S=str(n)
        m=0
        r=0
        for i in S:
                j=int(i)
                if(j%2==0):
                        r=r+1
                        if(r>m):
                                m=r
                else:
                        r=0
        return(m)





