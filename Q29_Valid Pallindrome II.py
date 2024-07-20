class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Check both cases by removing either character
                skip_left = s[l+1:r+1]  # Remove character at l
                skip_right = s[l:r]     # Remove character at r
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            l, r = l + 1, r - 1
        
        return True
