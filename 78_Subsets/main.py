#!/bin/python

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        res = []
        self.dfs(0, nums, res, [])
        return res

    def dfs(self, i, nums, res, subres):
        res.append(subres)
        #print(res)
        l = len(nums)
        for j in range(i, l):
            self.dfs(j+1, nums, res, subres + [nums[j]])
