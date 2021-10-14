def max_even_seq(n):
    num = str(n)
    list1 = []
    list2 = []
    list4 = []
    for x in num:
        list1.append(x)  
    for z in list1:
        y = int(z)
        if y % 2 == 0:
            list2.append(1)
        else: list2.append(0)
    newstring = ""
    for m in list2:
        newstring += str(m)
    list3 = newstring.split("0")
    for p in list3:
        f = len(p)
        list4.append(f)
    return max(list4)





