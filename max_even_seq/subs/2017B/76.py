def max_even_seq(n):
    # Cast n to a string, then replace each odd number with a space character using the str.translate method
    oddless_n = str(n).translate(str.maketrans('13579', ' ' * 5))
    # Split the now oddless n string by space characters into a list
    even_sequences = oddless_n.split()
    # If the list is empty, n had no even sequences
    if not even_sequences:
        return 0
    # Create a list of even sequence lengths using a list comprehension
    even_sequence_lens = [len(even_sequence) for even_sequence in even_sequences]
    # Return the largest sequence length in the length list
    return max(even_sequence_lens)




