def sum_of_intervals(intervals):
    add = 0
    rep = set()
    for x in intervals:
        for y in range(x[0], x[1]):
            if y not in rep:
                add += 1
            rep.add(y)
    return add 

print (sum_of_intervals([(1, 5), (6, 10)]))