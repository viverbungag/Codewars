def parse_int(string):
    word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven","twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    num = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20, 30, 40, 50, 60, 70, 80, 90]


    string = string.replace("-", " ")
    splitted = string.split(" ")
    ans = 0
    for x in range(len(splitted)):
        if splitted[x] in word:
            ans += num[word.index(splitted[x])]
        if splitted[x] == "thousand":
            ans *= 1000
            if "hundred" in splitted:
                if splitted.index("thousand") < splitted.index("hundred"):
                    ans /= 100
                if splitted.count("hundred") > 1:
                    ans /= 100
        if splitted[x] == "hundred":
            ans *= 100
        if splitted[x] == "million":
            ans *= 1000000

    return ans



print (parse_int('two hundred forty-six'))