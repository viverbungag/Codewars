def find_even_index(arr): return [x for x in range(len(arr)) if sum(arr[x+1:]) == sum(arr[:x])][0] if [x for x in range(len(arr)) if sum(arr[x+1:]) == sum(arr[:x])] else -1


print (find_even_index([-1,-2,-3,-4,-3,-2,-1]))