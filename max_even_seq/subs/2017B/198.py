def max_even_seq(n):
    """
    the function cauculate how many even
    numbers in a row are in the number
    gets the number n int to check the even numbers 
    """
    str_n = str(n)
    cnt = 0
    best_cnt = 0
    for num in str_n:
        #check if the number is even
        if eval(num+"%2==0"):
           cnt+=1
           #check if its the best even numbers in a row
           if cnt>best_cnt:
               best_cnt = cnt
        else:
            cnt=0
    return best_cnt




