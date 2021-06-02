def to_jaden_case(string):
    return " ".join([x.capitalize() for x in string.split(" ")])

quote = "How can mirrors be real if our eyes aren't real"
print (to_jaden_case(quote))