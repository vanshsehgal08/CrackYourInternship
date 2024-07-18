from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left<right:
                threeSum = num+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    res.append([num,nums[left],nums[right]])
                    left+=1
                    # [-2,-2,0,0,2,2]
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return res
