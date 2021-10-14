def max_even_seq(n):
    n_as_str = str(n)
    even_nums_sequences = [0]
    for i in range(0,len(n_as_str)):
        if int(n_as_str[i])%2==0:
            even_nums_sequences[-1] = even_nums_sequences[-1] + 1
        else:
            even_nums_sequences.append(0)
    return(max(even_nums_sequences))
        
