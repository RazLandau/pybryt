def max_even_seq(n):
    seq = [0]
    num = str(n)
    temp_seq = 0
    for dial in num:
        if int(dial)%2 == 0:
            temp_seq = temp_seq + 1
            num = num[1:]
        else:
            if int(temp_seq) > 0:
                seq.append(temp_seq)
            temp_seq = 0
            num = num[1:]
    seq.append(temp_seq)
    return max(seq)
            
            





