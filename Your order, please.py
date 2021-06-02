def getnum(x):
    for y in x:
        if y.isdigit():
            return y
def order(sentence):
  return " ".join(sorted(sentence.split(" "), key = getnum))

print (order("is2 Thi1s T4est 3a"))