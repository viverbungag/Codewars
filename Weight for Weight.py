def order_weight(string):
    list = string.split()
    summ = []
    dict = {}
    result = ""
    for x in range(len(list)):
        tot = 0
        for y in range (len(list[x])):
            tot += int(list[x][y])
        summ.append([tot, list[x]])
    summ.sort(key = lambda elem: elem[0])
    for x in range(len(summ)):
        summ[x][0] = str(summ[x][0])
        summ[x][1] = str(summ[x][1])

    for y in range(len(summ)):
        for x in range(len(summ)-y-1):
            if x < len(summ)-1:
                if summ[x][0] == summ[x+1][0]:
                    if summ[x][1] > summ[x+1][1]:
                        summ[x][1], summ[x+1][1] = summ[x+1][1], summ[x][1]
                    
    for x in range(len(summ)):
        if x < len(summ)-1:
            result += summ[x][1] + " "
        else:
            result += summ[x][1]
    return result




print (order_weight('1 2 200 4 4 6 6 7 7 18 27 72 81 9 91 425 31064 7920 67407 96488 34608557 71899703'))
        

        

            
            