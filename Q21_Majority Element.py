class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == e:
                count += 1
            else:
                count -= 1
                if count == 0:
                    e = nums[i]
                    count = 1
        return e
