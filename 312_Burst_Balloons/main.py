"""
o(N ^ 3) time
o(N ^ 2) space

1. define subproblems
dp[i][j] : the maximum coins we can collect by bursting all the balloons in nums[i:j+1]
number of subproblems o(N ^ 2)

2. guess
What is the last balloon to burst in nums[i:j+1]
number of choices o(j - i + 1) or o(N)

3. relate subproblem solutions
i - 1, i, i + 1, ... , k - 1, k, k + 1, ..., j - 1, j, j + 1
       ---------------------     --------------------
              dp[i][k - 1]            dp[k + 1][j]
              
dp[i][j] = max(dp[i][k - 1] + nums[i - 1] * nums[k] * [j + 1] + dp[k + 1][j])  i <= k <= j
corner case: i == k == j, dp[i][i - 1] and dp[k + 1][j] initialized to zero --> same equation
time per subproblem o(j - i) or O(N)

4. topological order
length from 1 to n

5. original problem
1, X, ..., X    , X, 1      nums
0, 1, ..., n - 1, n, n + 1  index
   ----------------
      dp[1][n]
"""

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for j in range(n + 2)] for i in range(n + 2)]
        
        def DP(i, j):
            if dp[i][j] > 0: return dp[i][j]
            for k in range(i, j+1):
                dp[i][j] = max(dp[i][j], DP(i, k-1) + nums[i-1] * nums[k] * nums[j+1]+ DP(k+1, j))
            return dp[i][j]
        
        return DP(1,n)
