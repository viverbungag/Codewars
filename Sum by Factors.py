from collections import defaultdict

def prime(x):
    if x % 2 == 0:
        return False
    for y in range(3, int(x**0.5) + 1, 2):
        if x % y == 0:
            return False
    return True

def sum_for_list(lst):
    arrPrime = [2]
    store = defaultdict(list)
    ans = []
    lstPositive = [abs(x) for x in lst]
    print (lstPositive)
    for x in range(3, (max(lstPositive)) + 1):
        if prime(x):
            arrPrime.append(x)
    for x in range(len(lst)):
        for y in range(len(arrPrime)):
            if lstPositive[x] % arrPrime[y] == 0:
                store[arrPrime[y]].append(lst[x])
    
    for x in store:
        ans.append([x, sum(store[x])])

    ans.sort(key=lambda x: x[0])
    return ans

print (sum_for_list([-29804, -4209, -28265, -72769, -31744]))