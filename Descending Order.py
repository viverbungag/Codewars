def descending_order(num):
    return int("".join(sorted(list(map(str, str(num))), reverse = True)))

print (descending_order(123456789))