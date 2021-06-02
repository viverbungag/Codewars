
def mix(s1, s2):
    sortArr = []
    store1 = {}
    store2 = {}
    ans = ""
    for x in s1:
        if x.isalpha() and x.islower():
            cnt = s1.count(x)
            if cnt > 1:
                store1[x] = cnt

    for x in s2:
        if x.isalpha() and x.islower():
            cnt = s2.count(x)
            if cnt > 1:
                store2[x] = cnt

    for x in store1:
        temp = ""
        if x in store2:
            if store1[x] > store2[x]:
                for y in range(store1[x]):
                    temp += x
                sortArr.append(["1", temp, y])
            if store1[x] == store2[x]:
                for y in range(store1[x]):
                    temp += x 
                sortArr.append(["=", temp, y])
        else:
            for y in range(store1[x]):
                temp += x
            sortArr.append(["1", temp, y])
    

    for x in store2:
        temp = ""
        if x in store1:
            if store2[x] > store1[x]:
                for y in range(store2[x]):
                    temp += x
                sortArr.append(["2", temp, y])
        else:
            for y in range(store2[x]):
                temp += x
            sortArr.append(["2", temp, y])
    
    sortArr.sort(key = lambda x: x[1])
    sortArr.sort(key = lambda x: x[0])
    sortArr.sort(key = lambda x: x[2], reverse=True)
    for x in sortArr:
        ans += f"{x[0]}:{x[1]}/"

    return ans[:-1]


print (mix("Are they here", "yes, they are here"))