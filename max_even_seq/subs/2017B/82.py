def max_even_seq(n):
    # Check if int is given
    if type(n) == int:
        cnt_max = 0
        data_list = []
        
        if n == 0:
            return 1
        else:
            # Convert n to string
            num = str(n)
            
            for i in num:
                # Check if even
                if int(i)%2 == 0:
                    cnt_max += 1
                    
                # Check if cnt_max != 0 (i is odd)
                elif cnt_max:
                    data_list.append(cnt_max)
                    # Restart counter
                    cnt_max = 0
                    
            data_list.append(cnt_max)
            return max(data_list)


