class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0:
            return [[]]
        results = []
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
    
    def dfs(self, nums, idx, subsets, results):
        results.append(list(subsets))
        for i in range(idx, len(nums)):
            if i-1 >= 0 and nums[i] == nums[i-1] and i > idx:
                continue
            subsets.append(nums[i])
            self.dfs(nums, i+1, subsets, results)
            subsets.pop()
