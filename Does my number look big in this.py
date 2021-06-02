def narcissistic( value ):
    # Code away
    length = len(str(value))
    ans = 0
    for x in str(value):
        ans += int(x) ** length
    if ans == value:
        return True
    return False

print (narcissistic(371))