
def days_represented(trips):
    ans = set()
    for x in trips:
        for y in range (x[0], x[1]+1):
            if y not in ans:
                ans.add(y)
                ans.add(y)
    return len(ans)



print (days_represented([[142, 174], [138, 151]])) #answer must be 37

#number of days represented in a year has a maximum of 365