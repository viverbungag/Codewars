def anagrams(word, words):
    ans = []
    word = list(map(str, word))
    word.sort()
    for x in words:
        chck = list(map(str, x))
        chck.sort()
        if word == chck:
            ans.append(x)
    return ans
    #your code here

print (anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))