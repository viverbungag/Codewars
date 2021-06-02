def find_num(n):
    if n <= 10:
        return n
    n = n + 1
    seq = []
    nxt = 0
    for x in range (n):
        num = 0
        while True:
            chck = True
            if num not in seq:
                for x in str(nxt):
                    for y in str(num):
                        if x == y:
                            chck = False
            else:
                chck = False
            if chck:
                print(num)
                seq.append(num)
                nxt = num
                break
            num += 1
    print (seq)
    return seq[n-1]



print (find_num(500))