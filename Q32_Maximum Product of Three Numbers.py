from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n < 3:
            return -1
        
        prod1 = nums[-1] * nums[-2] * nums[-3]
        prod2 = nums[0] * nums[1] * nums[-1]
    
        return max(prod1, prod2)
