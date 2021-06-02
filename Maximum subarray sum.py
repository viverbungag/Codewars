def max_sequence(arr):
	# ... 
    ans = 0
    for x in range(len(arr)):
        DetectMax = [0]
        num = 0
        for y in range(x, len(arr)):
            num += arr[y]
            DetectMax.append(num)
        if max(DetectMax) > ans:
            ans = max(DetectMax)
    return ans

print (max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))