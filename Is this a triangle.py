def is_triangle(a, b, c):
    return True if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0 else False

print (is_triangle(1, 2, 2))