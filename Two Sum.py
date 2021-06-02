def two_sum(numbers, target):
    for x in range (len(numbers)):
        for y in range (len(numbers)):
            if x != y:
                if numbers[x] + numbers[y] == target:
                    return [x, y]


print (two_sum([2,2,3], 4))