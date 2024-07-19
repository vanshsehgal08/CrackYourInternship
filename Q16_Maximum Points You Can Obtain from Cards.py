class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        lsum=0
        maxsum=0
        
        lsum = sum(cardPoints[:k])
        maxsum=lsum
        
        rindex=n-1
        rsum=0
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            rindex-=1
            maxsum=max(lsum+rsum,maxsum)
        return maxsum
        