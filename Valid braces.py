def validBraces(string):
    ident = False
    string_list = list(map(str, string))
    reverse_list = string_list.copy()
    reverse_list.reverse()
    num = 1
    for x in range(len(string_list)):
        if "(" == string_list[x]:
            if string_list[x] == "(" and reverse_list[x] == ")":
                ident = True
            elif string_list[x] == "(" and string_list[x+num] == ")":
                ident = True
            else:
                ident = False
                break
            if string_list.index("(") > string_list.index(")"):
                ident = False
                break

        if "[" == string_list[x]:
            if string_list[x] == "[" and reverse_list[x] == "]":
                ident = True
            elif string_list[x] == "[" and string_list[x+num] == "]":
                ident = True
            else:
                ident = False
                break
            if string_list.index("[") > string_list.index("]"):
                ident = False
                break

        if "{" == string_list[x]:
            if string_list[x] == "{" and reverse_list[x] == "}":
                ident = True
            elif string_list[x] == "{" and string_list[x+num] == "}":
                ident = True
            else:
                ident = False
                break
            if string_list.index("{") > string_list.index("}"):
                ident = False
                break

        if x == len(string_list)-1:
            num = 0

    return ident