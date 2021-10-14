def max_even_seq(n):
    max_seq = 0
    current_seq = 0
    even_num = [0,2,4,6,8]
    odd_num = [1,3,5,7,9]
    for num in str(n):
        if int(num) in even_num:
            current_seq = current_seq + 1
            max_seq = max(max_seq, current_seq)
        elif int(num) in odd_num:
            max_seq = max(max_seq, current_seq)
            current_seq = 0
    return max_seq