from itertools import combinations
def choose_best_sum(t, k, ls):
    # your code
    count = 0
    num = t
    ls.sort()
    print (ls)
    for x in ls:
        if count == k:
            break
        print (num)
        num -= x
        count += 1
    if num < 0:
        return None

    combs = combinations(ls, k)
    ans = 0
    for x in combs:
        if sum(x) <= t:
            if sum(x) > ans:
                ans = sum(x)

    if ans:
        return ans
    return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print (choose_best_sum(430, 8, xs))