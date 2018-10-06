class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo, hi = 0, x
        while lo <= hi:
            mid = lo + (hi-lo)/2
            if mid * mid == x:
                return mid
            if lo <= hi and mid * mid < x:
                lo = mid + 1
            if lo <= hi and mid * mid > x:
                hi = mid - 1
        if hi * hi < x:
            return hi
        if lo * lo < x:
            return lo
