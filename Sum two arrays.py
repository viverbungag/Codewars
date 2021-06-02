def sum_arrays(array1,array2):
    # write your code here
    if array1 and array2:
        string1 = ""
        string2 = ""
        for x in array1:
            string1 += str(x)
        for x in array2:
            string2 += str(x)
        print (string2)
        sum = str(int(string1) + int(string2))
        neg = False
        ans = []
        for x in sum:
            if x == "-":
                neg = True
                continue
            if neg:
                ans.append(int("-" + x))
                neg = False
            else:
                ans.append(int(x))
        return ans
        
    elif array1 and not array2:
        return array1
    elif array2 and not array1:
        return array2
    else:
        return []

print (sum_arrays([3, 2, 6, 6],[-7, 2, 2, 8]))