from itertools import permutations
def next_smaller(n):
    #your code here
    ans = ""
    converted  = list(map(str, str(n)))
    arr = []
    store = set()
    comp = ""
    for x in range(len(converted)-1, -1, -1):
        if x > 0:
            if converted[x] < converted[x-1]:
                for y in range(x-1, len(converted)):
                    arr.append(int(converted[y]))
                    comp += str(converted[y])
                perm = list(permutations(arr))
                print (perm)
                for a in perm:
                    wrd = ""
                    for b in a:
                        wrd += str(b)
                    if int(wrd) < int(comp):
                        store.add(int(wrd))
                if arr:
                    return int(str(n)[:x-1] + str(max(store)))
    return -1
    


print (next_smaller(1234567908))