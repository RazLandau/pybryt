def max_even_seq(n):
    mymax = 0
    current_seq = 0
    for i in str(n):
        if int(i) % 2 == 0 :
            current_seq = current_seq + 1
        else:
            current_seq = 0
        if current_seq > mymax:
            mymax = current_seq
    return mymax
    





