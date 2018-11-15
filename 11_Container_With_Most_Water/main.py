class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 2: return 0
        ans = 0
        l, r = 0, len(height)-1
        while l < r:
            h = min(height[l], height[r])
            ans = max(ans, h * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
