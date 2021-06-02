def rot13(message):
    ans = ""
    add = "abcdefghijklmABCDEFGHIJKLM"
    for x in message:
        if x.isalpha():
            if x in add:
                ans += chr(ord(x)+13)
            else:
                ans += chr(ord(x)-13)
        else:
            ans += x
    return ans

print (rot13("test"))

# print (chr(ord("m")+13))