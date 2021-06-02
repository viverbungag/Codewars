def pig_it(text):
    arr = text.split(" ")
    ans = ""
    boole = False
    for x in arr:
        strng = ""
        for y in range(len(x)):
            if not x[y].isalnum():
                boole = True
            if y > 0:
                strng += x[y]
        ans += strng + x[0] + "ay "

    if boole:
        return ans[:-3]
    return ans[:-1]
    

print (pig_it('Pig latin is cool '))