def series_sum(n):
    # Happy Coding ^_^
    ans = [1] 
    tri = 0
    for x in range (1, n):
        tri += 3
        ans.append(1/(1+tri))

    ret = round(sum(ans), 2) if n != 0 else 0
    return "{:.2f}".format(ret)

print (series_sum(1))