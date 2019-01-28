import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points:
            heapq.heappush(heap, point)
        return heapq.nsmallest(K, heap, key=lambda v: v[0]*v[0]+v[1]*v[1])
        
