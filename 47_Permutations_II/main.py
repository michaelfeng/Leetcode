class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        results = []
        # nums.sort()
        visited = set([])
        self.dfs(nums, [], results, visited)
        return results
    
    def dfs(self, nums, subsets, results, visited):
        key = "".join(str(s) for s in subsets)
        if len(nums) == 0 and key not in visited:
            # print subsets,
            visited.add(key)
            return results.append(list(subsets))
        
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], subsets+[nums[i]], results, visited)
        
