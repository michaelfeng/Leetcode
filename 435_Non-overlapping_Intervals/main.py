# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # 1. Sort intervals by end value
        sortedIntervals = sorted(intervals, key=lambda x: x.end)
        
        # 2. Check overlapping and add count
        ans, lastValid = 0, 0
        for i in range(1, len(sortedIntervals)):
            if self.isOverlapping(sortedIntervals[lastValid], sortedIntervals[i]):
                ans += 1
            else:
                lastValid = i           
        return ans
        
    def isOverlapping(self, inter1, inter2):
        if inter1.end <= inter2.start:
            return False
        if inter2.start >= inter1.end:
            return False
        return True
        
        
        
