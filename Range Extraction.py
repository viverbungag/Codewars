def solution(args):
    # your code here
    prev = 0
    ans = ""
    arr = []
    for x in range(len(args)):
        print (arr)
        if args[x] not in arr:
            if x < len(args)-2:
                if args[x+2] == args[x]+2:
                    if x+2 == len(args):
                        end = args[x+2]
                    count = 0
                    for y in range(x+2,len(args)):
                        if args[x]+2+count == args[y]:
                            end = args[y]
                        else:
                            break
                        count += 1
                    arr += [x for x in range(args[x], end+1)]
                    ans += str(args[x]) + "-" + str(end) + ","
                else:
                    ans += str(args[x]) + ","
            else:
                ans += str(args[x]) + ","
        
    return ans[:-1]

print (solution([-91, -88, -86, -85, -84, -84, -80, -78, -75, -73, -72, -69, -66, -64, -63]))


# -91,-88,-86--83,-80,-78,-75,-73,-72,-69,-66,-64,-63