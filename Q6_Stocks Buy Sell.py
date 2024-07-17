class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)
        return maxPro