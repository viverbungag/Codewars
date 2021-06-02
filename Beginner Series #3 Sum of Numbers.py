def get_sum(a,b):
    return sum([x for x in range(a, b+1)]) if b > a else sum([x for x in range(a, b-1, -1)])

print (get_sum(0,-1))