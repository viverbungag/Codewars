def array_diff(a, b):
        
    for x in range(len(b)):
        if b[x] in a:
            for _ in range(a.count(b[x])):
                a.remove(b[x])
    
    return a