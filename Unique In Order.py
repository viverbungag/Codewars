def unique_in_order(iterable):
    a = list(map(str, iterable))
    b = []
    int_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for x in range(len(a)):
        if x == len(a)-1:
                b.append(a[x])            
        else:
            if a[x+1] != a[x]:
                b.append(a[x])
                
    for x in range(len(b)):
        if b[x] in int_num:
            b[x] = int(b[x])

    return b