from math import factorial
def zeros(n):
    fact = str(n*(n-1))
    ans = 0
    count = 0
    print (fact)
    for x in fact:
        if x == "0":
            count += 1
            ans = count
        else:
            count = 0
    return ans


print (zeros(12))

print (factorial(12))