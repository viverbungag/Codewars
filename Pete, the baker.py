def cakes(recipe, available):
    ans = 0
    arr = []
    for x in recipe:
        if x in available:
            arr.append(available[x] // recipe[x])
        else:
            return 0
    return min(arr)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print (cakes(recipe, available))