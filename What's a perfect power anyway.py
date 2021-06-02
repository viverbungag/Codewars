def isPP(n):
    ans = []

    for x in range (2, n):
        for y in range (2 ,n):
            if pow(x, y) > n:
                break
            if pow(x, y) == n:
                ans.append(x)
                ans.append(y)
                return ans
    return None
    
            
print (isPP(484))
