def friend(a):
    new = []
    for x in range(len(a)):
        if len(a[x]) == 4:
            new.append(a[x])
    return new