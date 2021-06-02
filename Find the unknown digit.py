

def ifEqual(splitted, op, x, splitNum, num):
    rep0 = splitted[1].replace("?", str(x))
    if op in splitted[0]:
        mult = splitted[0].split(op, splitNum)
        rep1 = mult[0+num].replace("?", str(x))
        rep2 = mult[1+num].replace("?", str(x))
    if op == "+":
        if int(rep0) == int(rep1) + int(rep2):
            print(x)
            return True
    elif op == "*":
        if int(rep0) == int(rep1) * int(rep2):
            print(x)
            return True
    elif op == "-":
        if num == 1:
            if int(rep0) == int("-" + rep1) - int(rep2):
                print(x)
                return True
        else:
            if int(rep0) == int(rep1) - int(rep2):
                print(x)
                return True
    return False

def solve_runes(runes):
    # Your code here
    print(runes)
    splitted = runes.split("=")
    for x in range(10):
        if str(x) in runes:
            continue
        if x == 0:
            if "??" in splitted[1][:2]:
                continue
            if "-?" in splitted[1]:
                continue
        if "*" in splitted[0]:
            if ifEqual(splitted, "*", x, 1, 0):
                return x
        elif "+" in splitted[0]:
            if ifEqual(splitted, "+", x, 1, 0):
                return x
        elif "-"in splitted[0]:
            if splitted[0][0] == "-":
                if ifEqual(splitted, "-", x, 2, 1):
                    return x
            else:
                if ifEqual(splitted, "-", x, 1, 0):
                    return x

    print(-1)
    return -1



print (solve_runes("-7715?5--484?00=-28?9?5"))