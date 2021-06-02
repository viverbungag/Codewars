def score(dice):
    ans = 0
    if dice.count(1) == 3:
        ans += 1000
    if dice.count(2) >= 3:
        ans += 200
    if dice.count(3) >= 3:
        ans += 300
    if dice.count(4) >= 3:
        ans += 400
    if dice.count(5) == 3:
        ans += 500
    if dice.count(6) >= 3:
        ans += 600
    if dice.count(1) == 1:
        ans += 100
    if dice.count(1) == 2:
        ans += 200
    if dice.count(1) == 4:
        ans += 1100
    if dice.count(1) == 5:
        ans += 1200
    if dice.count(5) == 1:
        ans += 50
    if dice.count(5) == 2:
        ans += 100
    if dice.count(5) == 4:
        ans += 550
    if dice.count(5) == 5:
        ans += 600
    return ans

print (score([4, 4, 4, 3, 3]))