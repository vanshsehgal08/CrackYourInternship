class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            # Shorten the prefix
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix