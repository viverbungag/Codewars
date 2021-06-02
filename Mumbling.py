def accum(s):
    s = s.lower()
    output = ""
    for x in range (len(s)):
        for y in range(x+1):
            if y == 0:
                output += s[x].upper()
            else:
                output += s[x]
        if x != len(s)-1:
            output += "-"
    return output