from statistics import median


########################################################################

def partitions_dp(n):
    partitions_of = []
    partitions_of.append([()])
    partitions_of.append([(1,)])
    for num in range(2, n+1):
        ptitions = set()
        for i in range(num):
            for partition in partitions_of[i]:
                ptitions.add(tuple(sorted((num - i, ) + partition)))
        partitions_of.append(list(ptitions))
    return partitions_of[n]

########################################################################

def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

########################################################################

def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

########################################################################

def part(n):
    lst = list(accel_asc(n))
    arr = set()
    for x in lst:
        prod = 1
        for y in x:
            prod *= y
        arr.add(prod)
    arr = sorted(arr)
    Range = max(arr) - min(arr) 
    Avg = "{:.2f}".format(sum(arr)/len(arr))
    Median =  "{:.2f}".format(median(arr))
    return f"Range: {Range} Average: {Avg} Median: {Median}"

print (part(40))
