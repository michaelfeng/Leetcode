class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        n = len(prices)
        lowPrice = prices[0]
        maxProfit = 0
        for i in range(1, n):
            lowPrice = min(lowPrice, prices[i])
            maxProfit = max(maxProfit, prices[i]-lowPrice)
        
        return maxProfit
            
        
