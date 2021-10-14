def max_even_seq(n):
    num = str(n)
    even_seq_list = []
    cnt = 1
    for i in range(len(num)):
        if (int(num[i]))%2 == 0 and (int(num[i-1]))%2 == 0:
            cnt += 1
        elif (int(num[i]))%2 != 0 or i == len(num)-1:
            even_seq_list.append(cnt)
            cnt = 1
    if max(even_seq_list) > 1:
        return max(even_seq_list)
    else:
        if ('0' or '2' or '4' or '6' or '8') in num:
            return 1
        else:
            return 0
    
                


