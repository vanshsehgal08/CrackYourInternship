class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0
        mod_map = {0: 1}

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            
            # Ensure mod is positive
            if mod < 0:
                mod += k
            
            if mod in mod_map:
                count += mod_map[mod]
                mod_map[mod] += 1
            else:
                mod_map[mod] = 1
        
        return count