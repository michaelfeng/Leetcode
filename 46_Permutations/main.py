class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        results = []
        self.dfs(nums, [], results)
        return results
    
    def dfs(self, nums, subsets, results):
        if len(nums) == 0:
            return results.append(subsets)
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], subsets+[nums[i]], results)
        
