def is_isogram(string):
    return True if sum([1 for x in string.lower() if string.lower().count(x) > 1]) == 0 else False