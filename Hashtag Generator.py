def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    else:
        str = "#"
        for x in range(len(s)):
            if s[x-1].isspace() or x == 0:
                str += s[x].upper()
            else:
                str += s[x].lower()
        return str.replace(" ", "")