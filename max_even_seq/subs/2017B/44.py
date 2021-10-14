def max_even_seq(n):
    # we're gonna cast n to string and replace every odd number with a space, this way every viable sequeance of even number
    # will be seperated by at least space. we then split the string and return the max length
    my_string = str(n)
    for i in range(1,10,2):
	    my_string = my_string.replace(str(i), " ")
    if my_string == " "*len(str(n)):
            return 0
    return max([len(seq) for seq in my_string.split()])

