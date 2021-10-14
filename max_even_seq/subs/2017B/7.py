def max_even_seq(n):
    str_num = input("Please enter a positive integer:") #str type
    num = int(str_num)
    length = (len(str_num)) #int type
    list_even = []

    list_even_index = []
    rev_even_index = list_even_index.reverse()
    m = 0
    n = 0
    for i in range(0 , length):
        index = length - i
    if num%2 == 0:
        m = m+1
        num = num//10
        if num != 0:
            list_even.insert(n , m)
            n = n+1
            list_even_index.insert(n , index-1)
    elif num != 0 and num%2 == 0:
        list_even.insert(n , m)
        n = n+1
        list_even_index.insert(n , index)
        m = 0
        num = num//10

        list_even.reverse()
        list_even_index.reverse()

        length = max(list_even)
        start = list_even_index[list_even.index(length)]
        seq = str_num[start:start + length]

    if length > 0:
        print("The maximal even length is" , length)
        print("Sequence starts at" , start)
        print("Sequence is" , seq) 

