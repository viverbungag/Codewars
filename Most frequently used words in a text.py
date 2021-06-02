import re
def top_3_words(text):
    if not re.findall("\w", text):
        return []
    store = dict()
    ans = []
    text = re.sub("[^a-zA-Z ']", " ", text)
    splitted = text.split(" ")
    for x in splitted:
        if x != "":
            store[x] = splitted.count(x)
    store = dict(sorted(store.items(), key =lambda x: x[0].lower()))
    store = sorted(store.items(), key =lambda x: x[1], reverse = True)
    for x in range(3):
        if x < len(store):
            ans.append(store[x][0].lower())
    return ans


print (top_3_words("'''a"))