# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1 and isBadVersion(1): return 1
        
        start = 0
        end = n
        mid = (start + end) / 2
        
        while start <= end:
            midVal = isBadVersion(mid)
            if midVal and not isBadVersion(mid - 1):
                return mid
            
            if midVal:
                end = mid - 1
            else:
                start = mid + 1
            
            mid = (start + end) / 2
        
        return -1
