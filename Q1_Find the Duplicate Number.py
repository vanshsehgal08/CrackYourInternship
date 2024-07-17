class Solution(object):
    def findDuplicate(self, nums):
        # Phase 1
        slow=nums[0]
        fast=nums[0]
        
        # Move slow by 1 step and fast by 2 steps
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        # Phase 2
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return fast
        

        