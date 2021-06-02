def maskify(cc):
    return "".join([cc[x] if x > len(cc)-5 else "#" for x in range(len(cc))])

print ( maskify("12345"))
    