def filter_list(l):
    return [x for x in l if type(x) == int]

print (filter_list([1,2,'a','b', "12"]))