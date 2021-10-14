def max_even_seq(n):
    n_list = [int(num) for num in str(n)] # list of numbers in n
    counter = 0
    seq_even = []
    i = 0
    
    for i in range(0, len(n_list)):
        #check if even and end of list
        if (n_list[i]%2 == 0) and (i == len(n_list)-1):
            counter += 1
            seq_even.append(counter)

        if (n_list[i]%2 == 0):
            counter += 1
            
        else:
            seq_even.append(counter)
            counter = 0

    return(max(seq_even))




