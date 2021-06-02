
def steps(num):
    for x in range(num//2,0, -1):
        if num % x == 0:
            print (x)
            return x


def factor(num):
    # your code
    start = int((num**0.5)/4)
    end = int(num**0.5)+1
    step = steps(num)
    for x in range(start, end, step):
        for y in range(start, end, step):
            if x**2 + y**2 == num:
                return [x, y]

def solve(arr):
    prod = []
    ans = 1
    for x in range(0, len(arr), 2):
        ans *= ((arr[x] * arr[x]) + (arr[x+1] * arr[x+1]))
    
    print (prod)
    print (ans)
    return factor(ans)

print (solve([3, 9, 8, 4, 6, 8, 7, 8, 4, 8, 5, 6, 6, 4, 4, 5]))