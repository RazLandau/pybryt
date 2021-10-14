def max_even_seq(n):
    n_str = str(n)
    bigger_seq = 0
    actual_seq = 0
    for i in range(len(n_str)):
        if (int(n_str[i])%2 == 0): # if even
            actual_seq = actual_seq + 1
        else:
            if (actual_seq > bigger_seq):
                bigger_seq = actual_seq #this is the new bigger sequence
                actual_seq = 0 #zero and search for new sequence
    #last check
    if (actual_seq > bigger_seq):
        bigger_seq = actual_seq #this is the new bigger sequence
        actual_seq = 0 #zero and search for new sequence
    return bigger_seq
            





