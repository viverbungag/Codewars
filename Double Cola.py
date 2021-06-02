def who_is_next(names, r):
    # your code
    if r <= len(names):
        return names[r-1]
    num = len(names)
    prod = num
    sub = num
    while True:
        if prod*2 + sub > r:
            sub = r - sub
            break
        prod *= 2
        sub += prod

    bin = (prod*2)//num
    return names[(sub-1)//bin]

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]



print (who_is_next(names, 30))