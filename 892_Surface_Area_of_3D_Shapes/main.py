class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        if not grid[0]: return 0
        
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += self.countArea(grid[i][j])
                if i: ans -= min(grid[i][j], grid[i - 1][j]) * 2
                if j: ans -= min(grid[i][j], grid[i][j - 1]) * 2
        return ans
        
    def countArea(self, v):
        if v == 0: return 0
        if v >= 1:
            return 2+v*4
        
