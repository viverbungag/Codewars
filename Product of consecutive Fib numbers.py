
def fib():
    prev1 = 0
    prev2 = 1
    while True:
        equal = prev1 + prev2
        prev1 = prev2
        prev2 = equal
        yield prev1

def productFib(prod):
    # your code
    prev = 0
    for x in fib():
        if x * prev == prod:
            return [prev, x, True]
        elif x * prev > prod:
            return [prev, x, False]
        prev = x


print(productFib(5895))