def is_prime(num):
    if num == 2:
        return True
    if num == 0 or num == 1 or num < 0 or num % 2 == 0:
        return False
    for x in range (3, (num//2) + 1, 2):
        if num % x == 0:
            return False
        if x*x > num:
            break
    return True


print (is_prime(6))

