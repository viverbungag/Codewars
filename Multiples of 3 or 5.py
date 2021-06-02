def solution(number):
    return sum([x for x in range(number-1, 2, -1) if x%3 == 0 or x%5 == 0])
        