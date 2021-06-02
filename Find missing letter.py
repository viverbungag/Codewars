def find_missing_letter(chars):
    compare = []
    diff = ord(chars[len(chars)-1]) - ord(chars[0]) + 1
    for x in range(diff):
        compare.append(chr(ord(chars[0]) + x))
    for x in compare:
        if x not in chars:
            letter = x
    return letter