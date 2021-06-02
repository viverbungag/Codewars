
def rec(sq,store, num):
    print (f"sq:{sq}")
    print (f"num:{num}")
    if sq == 0:
        return store
    if sq > 0 and num <= 0:
        return rec()
    if num ** 2 <= sq:
        store.add(num)
        return rec(sq-num**2, store, int(sq**0.5)-2)
    else:
        return rec(sq, store, num-1)
    


def decompose(n):
    print (n)
    # your code
    return rec(n**2, set(), n-1)

print(decompose(12))