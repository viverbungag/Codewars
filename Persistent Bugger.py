def persistence(n):
    count = 0
    while len(str(n)) != 1:
        temp = 1
        for x in str(n):
            temp *= int(x)
        n = temp
        count += 1
    return count

print (persistence(39))