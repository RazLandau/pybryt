def max_even_seq(n):
    str_num = input("Please enter a positive integer:") #str type
    num = int(str_num)
    length = (len(str_num)) #int type
    list_odds = []

    list_odds_index = []
    rev_odds_index = list_odds_index.reverse()

    j = 0
    k = 0
    for i in range(0 , length):
        index = length - i
        if num%2 != 0:
            j = j+1
            num = num//10
            if num == 0:
                list_odds.insert(k , j)
                k = k+1
                list_odds_index.insert(k , index-1)
        elif num != 0 and num%2 == 0:
            list_odds.insert(k , j)
            k = k+1
            list_odds_index.insert(k , index)
            j = 0
            num = num//10

    list_odds.reverse()
    list_odds_index.reverse()


    length = max(list_odds)
    start = list_odds_index[list_odds.index(length)]
    seq = str_num[start:start + length]
                                
    if length > 0:
        print("The maximal length is" , length)
        print("Sequence starts at" , start)
        print("Sequence is" , seq)   


