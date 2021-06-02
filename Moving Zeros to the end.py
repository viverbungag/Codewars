def move_zeros(array):
    #your code here
    copy = []
    zeroes = sum((x == 0 and x is not False) for x in array)
    for x in range(len(array)):
        if array[x] != 0 or array[x] is False:
            copy.append(array[x]) 
    for x in range (zeroes):
        copy.append(0)
    return copy

print (move_zeros([2,False,0,1,0,1,0,3,0,1]))