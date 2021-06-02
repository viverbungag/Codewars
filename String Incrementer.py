def increment_string(string):
    num = "1234567890"
    add = ""
    result = ""
    count = 0
    boole = False
    for x in string:
        if x.isnumeric():
            boole = True

    if boole:
        for x in range(len(string)-1, -1, -1):
            if string[x] not in num:
                saved = x+1
                break
            else:
                saved = 0
                
        for x in range(saved, len(string)):
            add += string[x]
            count += 1
        
        for x in range(saved):
            result += string[x]
    else:
        for x in range(len(string)):
            result += string[x]

    if add:
        added = int(add) + 1
    else:
        added = 1
    for x in range(len(str(added)), count):
        result += "0"

    result += str(added)
            
    return result


print (increment_string("foorbar09"))

