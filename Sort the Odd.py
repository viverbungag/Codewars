def sort_array(source_array):
    arrOdd = []
    arrEven = []
    for x in source_array:
        if x % 2 == 1:
            arrOdd.append(x)
        else:
            arrEven.append(x)
    arrOdd.sort()
    for x in arrEven:
        arrOdd.insert(source_array.index(x), x)
    return arrOdd
    # Return a sorted array.

print (sort_array([5, 3, 2, 8, 1, 4]))