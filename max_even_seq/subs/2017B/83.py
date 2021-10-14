def max_even_seq(n):
    # Vars
    c = 0;
    cMax = c;
    
    # Positify
    n = str(abs(n))
    # Going over the digits
    for char in n :
        # If this is an even digit
        if int(char) % 2 == 0:
            # Raise the counter
            c = c + 1;
        # If this is an odd digit
        else:
            # Reset the counter
            c = 0;
        # If current count is higher than max count
        if c>cMax:
            # Save current count value
            cMax = c;
    # Print count
    print (cMax);
        

