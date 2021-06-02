x = [12 ,24, 54 ,67, 2, 5]

for i in range(len(x)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(x)): 
        if x[min_idx] > x[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    x[i], x[min_idx] = x[min_idx], x[i]

 