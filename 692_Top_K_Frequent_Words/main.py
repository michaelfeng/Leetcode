import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap = []
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        
        for key, val in dic.items():
            heapq.heappush(heap, (-val, key))
        
        strs = heapq.nsmallest(k, heap)
        ans = [s[1] for s in strs]
        return ans
