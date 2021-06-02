def validate_battlefield(field):
    print(field)
    store = []
    excempt = []
    check = {4:0, 3:0, 2:0, 1:0}
    for x in range(10):
        for y in range(10):
            if field[x][y] == 1:
                store.append((x, y))
    for x in store:
        if x not in excempt:
            count1 = 1
            count2 = 1
            for y in range(1, 9):
                if (x[0]+y, x[1]) in store:
                    if (x[0]+y+1, x[1]+1) in store or (x[0]+y+1, x[1]-1) in store or (x[0]+y-2, x[1]+1) in store or (x[0]+y-2, x[1]-1) in store:
                        return False
                    count1 += 1
                    excempt.append((x[0]+y, x[1]))
                else:
                    break
            for y in range(1, 9):
                if (x[0], x[1]+y) in store:
                    if (x[0]-1, x[1]+y-2) in store or (x[0]+1, x[1]+y-2) in store or (x[0]-1, x[1]+y+1) in store or (x[0]+1, x[1]+y+1) in store:
                        return False
                    count2 += 1
                    excempt.append((x[0], x[1]+y))
                else:
                    break
            if count1 > 4 or count2 > 4:
                return False
            if count1 == 1 and count2 == 1:
                check[1] += 1
                if (x[0]+1, x[1]+1) in store and (x[0]-1, x[1]+1) in store and (x[0]+1, x[1]-1) in store and (x[0]-1, x[1]-1) in store:
                    return False
            else:
                if count1 > 1:
                    check[count1] += 1
                if count2 > 1:
                    check[count2] += 1
            
            excempt.append((x[0], x[1]))
    print (check)
    if check[4] == 1 and check[3] == 2 and check[2] == 3 and check[1] == 4:
        return True
    return False
battleField = [ [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1, 1, 0, 1, 0, 0]  ]

print (validate_battlefield(battleField))