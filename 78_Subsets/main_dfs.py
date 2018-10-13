import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # nums.sort()
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, idx, subset, result):
        result.append(copy.deepcopy(subset))
        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, result)
            subset.pop()
