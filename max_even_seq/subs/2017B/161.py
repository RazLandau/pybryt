def max_even_seq(n):
    strn = str(n)
    trutheven = []
    for digit in strn:
        if int(digit) % 2 == 0:
            trutheven.append('+')
        else:
            trutheven.append('-')
    count = 0
    seqlist = []
    for value in trutheven:
        if value == '-':
            count = count * 0
            seqlist.append(count)
        else:
            count = count + 1
            seqlist.append(count)
    max_even_seq1 = max(seqlist)
    return max_even_seq1




 #Testing Q6
