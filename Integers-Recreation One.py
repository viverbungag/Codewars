
def list_squared(m, n):
    # your code
    ans = []
    for x in range(m, n):
        div = 0
        for y in range(1, int((x**0.5)+1)):
            if x % y == 0:
                if(x / y == y):
                    div += (y**2)
                else:
                    div += (y**2) + ((x/y)**2)
        if (int(div**0.5) - (div**0.5)) == 0:
            ans.append([x, int(div)])
    return ans

print (list_squared(1, 250))