import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix: return 0
        if not matrix[0]: return 0
        
        heap = []
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                heapq.heappush(heap, matrix[i][j])
                
        ans = heapq.nsmallest(k, heap)
        return ans[k-1]
                
        
