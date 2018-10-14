class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        nums = [i+1 for i in range(n)]
        # print nums, n, k
        self.dfs(nums, k, 0, [], results)
        return results
    
    def dfs(self, nums, k, idx, subsets, results):
        if len(subsets) == k:
            results.append(list(subsets))
            return 
        
        for i in range(idx, len(nums)):
            subsets.append(nums[i])
            self.dfs(nums, k, i+1, subsets, results)
            subsets.pop()
