def max_even_seq(n):
    total = 0
    seq_list = [0]
    for i in str(n):
        if int(i)%2 == 0:
            total = total + 1
            seq_list.insert(0,total)
        else:
            total = 0
    return(max(seq_list))




