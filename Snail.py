
def snail(snailMap):
    length = sum([1 for x in snailMap for y in x])
    arr = []
    sub = 0
    while True:
        # print ("\ntop: ")
        for top in range(0 + sub, len(snailMap[0+sub]) - sub):
            # print (snailMap[0+sub][top], end =", ")
            arr.append(snailMap[0+sub][top])

        if length == len(arr):
            break
        
        # print ("\nright: ")
        for right in range(1 + sub, len(snailMap) - 1 - sub):
            # print (snailMap[right][-1 - sub], end =", ")
            arr.append(snailMap[right][-1 - sub])

        if length == len(arr):
            break

        # print ("\nbot: ")
        for bottom in range(len(snailMap[-1-sub]) - 1 -sub, -1 + sub, -1):
            # print (snailMap[-1-sub][bottom], end =", ")
            arr.append(snailMap[-1-sub][bottom])
            

        if length == len(arr):
            break

        # print ("\nleft: ")
        for left in range(len(snailMap) - 2 - sub, 0 + sub, -1):
            # print (snailMap[left][0 + sub], end =", ")
            arr.append(snailMap[left][0 + sub])

        if length == len(arr):
            break

        sub += 1

    return arr

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print (snail(array))