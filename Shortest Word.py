def find_short(s):
    return len(min(s.split(" "), key = len))

print (find_short("i want to travel the world writing code one day"))