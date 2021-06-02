def find_outlier(integers):
    return [x for x in integers if x % 2 == 0][0] if sum([1 for x in integers if x % 2 == 0]) == 1 else [x for x in integers if x % 2 == 1][0]

print (find_outlier([2, 4, 6, 8, 10, 3]))   