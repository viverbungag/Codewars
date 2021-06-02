def count_smileys(arr):
    ans = 0
    for x in arr:
        if x[0] == ":" or x[0] == ";":
            if x[1] == ")" or x[1] == "D":
                ans += 1
            elif x[1] == "~" or x[1] == "-":
                if x[2] == ")" or x[2] == "D":
                    ans += 1
    return ans


print (count_smileys([';]', ':[', ';*', ':$', ';-D']))