from itertools import product
def get_pins(observed):
    adj ={
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "4", "5", "6", "8"],
        "6": ["3", "5", "6", "9"],
        "7": ["4", "7", "8"],
        "8": ["5", "7", "8", "9", "0"],
        "9": ["6", "8", "9"],
        "0": ["8", "0"]
    }
    arr = []
    ans = []
    for x in range (len(observed)):
        temp = []
        for y in adj:
            if observed[x] == y:
                for z in adj[y]:
                    temp.append(z)
        arr.append(temp)
    print (arr)
    prd = list(product(*arr))
    for x in prd:
        wrd = ""
        for y in x:
            wrd += y
        ans.append(wrd)
    return ans

print (get_pins("46"))
  