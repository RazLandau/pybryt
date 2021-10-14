def max_even_seq(n):
    num_str = str(n)
    cnt = m = 0 
    for i in num_str:
        num1 = int(i) 
       
        if num1 % 2 == 0:
            cnt += 1  

        else:
            m = max(m, cnt) # m receives the longest sequence so far 
            cnt = 0
    return max(m, cnt) 
        
        



