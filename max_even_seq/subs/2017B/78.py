def max_even_seq(n):
    str_input=str(n)
    even_numbers=[]
    counter=0
    for i in range(len(str_input)):
        if int(str_input[i])%2==0:
            counter+=1
        else:
            even_numbers.append(counter)
            counter= 0
    even_numbers.append(counter)
    return max(even_numbers)

