def iq_test(numbers): 
    return [int(numbers.split(" ").index(x)) for x in numbers.split(" ") if int(x)%2 == 0][0]+1 if sum([1 for x in numbers.split(" ") if int(x)%2 == 0]) == 1 else [int(numbers.split(" ").index(x)) for x in numbers.split(" ") if int(x)%2 == 1][0]+1

print (iq_test("2 4 7 8 10")) 