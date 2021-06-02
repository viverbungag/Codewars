def high(x):
    sentence = x.split(" ")
    highest = 0
    for x in range (len(sentence)):
        value = 0
        for y in range (len(sentence[x])):
            value += (ord(sentence[x][y])-96)
            if value > highest:
                highest = value
                word = sentence[x]
    return word