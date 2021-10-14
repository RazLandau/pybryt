def max_even_seq(n):
    high_score = 0
    even_seq = 0
    for c in str(n):
        if int(c) % 2 == 0:
            even_seq += 1
        else:
            high_score = max(high_score, even_seq)
            even_seq = 0

    return high_score

