def spin_words(sentence):
    arr = sentence.split(" ")
    ans = []
    for x in arr:
        if len(x) > 4:
            ans.append("".join(reversed(list(map(str, x)))))
        else:
            ans.append(x)
    return " ".join(ans)

print (spin_words( "Hey fellow warriors"))