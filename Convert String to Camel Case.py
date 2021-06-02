def to_camel_case(text):
    #your code here
    text = text.replace("-", "_").split("_")
    ans = text[0]
    for x in text[1:]:
        ans += x.capitalize()
    return ans


print (to_camel_case("the_stealth_warrior"))