def first_non_repeating_letter(string):
    lst = list(map(str, string.casefold()))
    ans = ""
    for x in string:
        low = x.casefold()
        if lst.count(low) == 1:
            ans = x
            break
    return ans

print (first_non_repeating_letter('moonmen'))