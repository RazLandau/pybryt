def max_even_seq(n):
    if n == 0:
        return 1
    lst = []
    while n > 0 : # bulding a list from the %2 of the digits
        eventy = n % 2
        lst.append(eventy)
        n = n // 10
    max_seq = 0
    local_seq = 0
    for run in lst :
        if run == 0 :
            local_seq = local_seq + 1 #every time it meets zero it increases
        if run == 1 :
            local_seq = 0 #every time it meets number 1 it starting to count from the begining
        max_seq = max(max_seq, local_seq) 
    return max_seq
    




