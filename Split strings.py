def solution(s):
    list = []
    for x in range(0, len(s), 2):
        if x == len(s)-1 and len(s) % 2 == 1:
            str = s[x] + "_"
        else:
            str = s[x] + s[x+1]
        list.append(str)
    
    return list