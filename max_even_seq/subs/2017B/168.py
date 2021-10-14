def max_even_seq(n):
   nAsString = str(n)
   currentLength = maxLength = 0
   for CurrentDigit in nAsString:
      if int(CurrentDigit)%2==0: #is the current digit 'even' ?
         currentLength += 1
         if currentLength > maxLength:
            maxLength = currentLength
      else:
         currentLength = 0
   return(maxLength)


