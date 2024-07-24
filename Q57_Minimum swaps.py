class Solution:
    
    def minSwaps(self, nums):
        # Step 1: Create a sorted version of the array
        sorted_nums = sorted(nums)
        n = len(nums)
        
        # Step 2: Create a mapping from original indices to sorted indices
        index_map = {value: idx for idx, value in enumerate(sorted_nums)}
        
        # Step 3: Create a visited array to track elements already placed correctly
        visited = [False] * n
        
        # Step 4: Initialize the number of swaps
        swaps = 0
        
        # Step 5: Iterate through each element to find and count cycles
        for i in range(n):
            if visited[i] or index_map[nums[i]] == i:
                continue
            
            # Start a new cycle
            cycle_size = 0
            x = i
            
            while not visited[x]:
                visited[x] = True
                x = index_map[nums[x]]
                cycle_size += 1
            
            # If cycle size is greater than 1, add (cycle_size - 1) swaps
            if cycle_size > 1:
                swaps += (cycle_size - 1)
        
        return swaps
