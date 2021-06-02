def alphabet_position(text):
    return " ".join([str(ord(x)-96) for x in text.lower() if x.isalpha()])

print (alphabet_position("The sunset sets at twelve o' clock."))