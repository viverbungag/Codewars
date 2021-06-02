def solve(st):
    st = list(map(str, st))
    st.sort()
    init = min(st)
    num = ord(init)
    count = 0
    for x in range(num, num + len(st)):
        if ord(st[count]) != x:
            return False
        count += 1
    return True
    

print(solve("dabc"))