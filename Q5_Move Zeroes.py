class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                j=i
                break
        if j==-1:
            return nums
        for i in range(j+1,n):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
        
        