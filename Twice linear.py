def dbl_linear(n):
    store = [1]
    two = 0
    three = 0
    while len(store) <= n:
        form1 = 2 * store[two] + 1
        form2 = 3 * store[three] + 1
        if (form1) > (form2):
            store.append(form2)
            three += 1
        else:
            if form1 != form2:
                store.append(form1)
            two += 1
            
    return store[n]

print (dbl_linear(50))