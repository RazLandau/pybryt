def max_even_seq(n):
    even_list = []
    cnt_even = 0
    for digit in str(n):
        if int(digit)%2 == 0:
            cnt_even += 1
            even_list.append(cnt_even)
        else:
            cnt_even = 0
            even_list.append(cnt_even)

    return(max(even_list))

