def high_and_low(numbers):
    ans = ""
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    ans += str(max(numbers)) + " "
    ans += str(min(numbers)) 
    return ans

print (high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))