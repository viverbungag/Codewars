def sum_two_smallest_numbers(numbers):
    return sum([sorted(numbers)[0], sorted(numbers)[1]])

print (sum_two_smallest_numbers([5, 8, 12, 18, 22]))