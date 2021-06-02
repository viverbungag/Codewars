def fib():
    prev1 = 0
    prev2 = 1
    while True:
        equal = prev1 + prev2
        prev1 = prev2
        prev2 = equal
        yield prev1

def perimeter(n):
    # your code
    ans = 0
    for count, items in enumerate(fib()):
        if count <= n:
            ans += items
        else:
            break

    return ans*4
    
print (perimeter(100))