def is_square(n): 
    return True if n > -1 and int(n**0.5) == n**0.5 else False 


print (is_square(25))