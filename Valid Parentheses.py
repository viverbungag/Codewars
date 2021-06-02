def valid_parentheses(string):
    #your code here
    if not string:
        return True
    open = 0
    close = 0
    for x in string:
        if x == "(":
            open += 1
        if x == ")":
            close += 1

        if close > open:
            return False
    if close != open:
        return False
    if close == 0:
        return False
    return True


print (valid_parentheses("hi())("))     