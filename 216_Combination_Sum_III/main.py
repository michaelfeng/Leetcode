class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        A = [i for i in range(1,10)]
        results = []
        # A.sort()
        self.dfs(A, k ,n, 0, [], results)
        return results
    
    def dfs(self, A, k, target, idx, subsets, results):
        if target == 0 and len(subsets) == k:
            return results.append(list(subsets))
            
        for i in range(idx, len(A)):
            if target < A[i]:
                return
            subsets.append(A[i])
            self.dfs(A, k, target - A[i], i+1, subsets, results)
            subsets.pop()
