def find_next_square(sq):
    return int(((sq**0.5)+1)**2) if sq**0.5 == int(sq**0.5) else -1

print (find_next_square(155))