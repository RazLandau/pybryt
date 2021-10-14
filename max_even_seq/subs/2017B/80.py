def max_even_seq(n):
    '''
    max_even_seq (integer) --> integer
    return the maximun number of even digits sequence in n
    '''
    counter = 0
    save = 0
    for digit in str (n):
        if (int(digit))%2==0:
            counter+=1
        else:
            save = max(counter, save)
            counter=0
    return max (counter,save)
