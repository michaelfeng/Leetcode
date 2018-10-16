import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        visit = set([1])
        val = None
        for i in xrange(n):
            val = heapq.heappop(heap)
            for j in [2,3,5]:
                num = val * j
                if num not in visit:
                    visit.add(num)
                    heapq.heappush(heap, num)
        return val
