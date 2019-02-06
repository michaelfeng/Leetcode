class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])
        
