def longest_consec(strarr, k):
    # your code
    if not strarr or k < 1 or k > len(strarr):
        return ""
    arr = []
    for x in range(len(strarr)-k+1):
        strng = ""
        for y in range(x, x+k):
            strng += strarr[y]
        arr.append(strng)
    ans = max(arr, key=len)
    return ans
    

print (longest_consec([], 3))