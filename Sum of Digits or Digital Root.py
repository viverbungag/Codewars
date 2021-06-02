def digital_root(n):
    ans = str(n)
    while len(ans) != 1:
        temp = 0
        for x in ans:
            temp += int(x)
        ans = str(temp)

    return int(ans)

print (digital_root(942))