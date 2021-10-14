def max_even_seq(n):
    longest, current = 0, 0
    for evenp in map(lambda x: int(x)%2 == 0, str(n)):
        if evenp:
            current = current + 1
        else:
            current = 0
        longest = max(longest, current)
    return longest





