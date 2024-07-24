class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums)//2]
        res = sum([abs(x-med) for x in nums])
        return res
        