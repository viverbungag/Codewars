def solution(roman):
    ans = 0
    prev = 0
    rom = ["I", "V", "X", "L", "C", "D", "M"]
    val = [1, 5, 10, 50, 100, 500, 1000]
    for x in range (len(roman)):
        for y in range (len(rom)):
            if roman[x] == rom[y]:
                ans += val[y]
                if x != len(roman)-1:
                    prev = val[y]
            if x != len(roman)-1:
                if roman[x+1] == rom[y]:
                    if prev < val[y]:
                        ans -= (prev*2)
    return ans

print (solution('IX'))