# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end
        ans = []
        for interval in intervals:
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                ans.append(Interval(start, end))
                start, end = interval.start, interval.end
        
        ans.append(Interval(start, end))
        return ans
