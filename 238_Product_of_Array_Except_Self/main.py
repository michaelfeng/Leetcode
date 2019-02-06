class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 1
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res *= nums[i]
            else:
                zeroCount += 1
        ans = []
        if zeroCount > 1:
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if zeroCount == 1 and nums[i] != 0:
                ans.append(0)
            if zeroCount == 1 and nums[i] == 0:
                ans.append(res)
            if zeroCount == 0:
                ans.append(res/nums[i])
        return ans
    
    
