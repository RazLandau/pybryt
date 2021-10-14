def max_even_seq(n):
    if n > 0:
        even_nums = list() 
        counter = 0
        num = 0
        for i in str(n):
            if int(i)%2 == 0:
                num = counter + 1
                counter += 1
            else: 
                even_nums.append(num)
                counter = 0
        even_nums.append(num)
        return (max(even_nums))
    else:
        print ("Invalid number.")
        
