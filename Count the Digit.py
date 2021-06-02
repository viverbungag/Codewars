def nb_dig(n, d):
    # your code
    ans = 0
    arr = [x**2 for x in range(n+1)]
    for x in arr:
        chck = str(x)
        for y in chck:
            if y == str(d):
                ans += 1
    
    return ans

print (nb_dig(5750, 0))