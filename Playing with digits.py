def dig_pow(n, p): return sum([int(x)**(count+p) for count, x in enumerate(str(n))])//n if int(sum([int(x)**(count+p) for count, x in enumerate(str(n))])/n) == sum([int(x)**(count+p) for count, x in enumerate(str(n))])/n else -1 

print (dig_pow(46288, 3)) 