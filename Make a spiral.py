def spiralize(size):
    storeEven, addOrder1, addOrder2, orderh, orderh2, ans, count1, count2 = [], [], [], [], [], [], 0, 0
    for x in range(1, size//2+1, 2):
        storeEven.append(x)
    for x in range(size-2, size//2-1, -2):
        if x not in storeEven:
            storeEven.append(x)
    for x in range(1, size//2+1, 2):
        addOrder1.append(size-x)
        addOrder1.append(x-1)
    for x in range(2, size//2+1, 2):
        addOrder2.append(size-x)
        addOrder2.append(x-1)
    orderh = [x for x in range(1, len(storeEven)+1) if x%2 == 1] + [x for x in range(len(storeEven), 0, -1) if x%2 == 0]
    orderh2 = [x for x in range(1, size-len(storeEven)-1) if x%2 == 1] + [x for x in range(size-len(storeEven)-2, 0, -1) if x%2 == 0]
    for x in range(size):
        semiArr = []
        if x == 0 or x == size-1:
            for y in range(size):
                semiArr.append(1)
        elif x in storeEven:
            temp = [addOrder1[z] for z in range(orderh[count1])]
            for y in range(size):
                if y in temp:
                    semiArr.append(1)
                else:
                    semiArr.append(0)
            count1 += 1
        else:
            print(x)   
            temp = [addOrder2[z] for z in range(orderh2[count2])]
            for y in range(size):
                if y in temp:
                    semiArr.append(0)
                else:
                    semiArr.append(1)
            count2 += 1
        ans.append(semiArr)
    return ans


spiral = [  [1,1,1,1,1],
            [0,0,0,0,1],
            [1,1,1,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]   ]


spiral = [  [1,1,1,1,1,1],
            [0,0,0,0,0,1],
            [1,1,1,1,0,1],
            [1,0,0,1,0,1],
            [1,0,0,0,0,1],
            [1,1,1,1,1,1]   ]

spiral = [  [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,0,1],
            [1,0,0,0,0,1,0,1],
            [1,0,1,0,0,1,0,1],
            [1,0,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1]   ]


print (spiralize(8))


    # print(f"storeEven: {storeEven}")
    # print(f"addOrder1: {addOrder1}")
    # print(f"addOrder2: {addOrder2}")
    # print(f"orderh: {orderh}")
    # print(f"orderh2: {orderh2}")