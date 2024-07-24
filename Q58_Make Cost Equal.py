def min_cost_to_make_equal(arr):
    # Sort the array
    arr.sort()
    
    # Find the median
    n = len(arr)
    median = arr[n // 2]
    
    # Calculate the total cost
    cost = sum(abs(x - median) for x in arr)
    
    return cost

