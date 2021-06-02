def count_bits(n):
    return sum([1 for x in bin(n) if x == "1"])

print ( count_bits(1234))