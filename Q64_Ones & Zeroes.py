from collections import defaultdict

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = defaultdict(int)
        
        for i in range(len(strs)):
            s = strs[i]
            mCnt, nCnt = s.count("0"), s.count("1")
            # Traverse backwards to avoid overwriting previous states in the same iteration
            for M in range(m, mCnt - 1, -1):
                for N in range(n, nCnt - 1, -1):
                    dp[(M, N)] = max(dp[(M, N)], 1 + dp[(M - mCnt, N - nCnt)])
        
        return dp[(m, n)]