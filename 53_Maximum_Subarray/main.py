class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # f[i] maxSubarray(0..i)
        # f[i] = f[i-1] > 0 ? nums[i] + f[i-1] : nums[i]
        f = [0]*len(nums)
        f[0] = nums[0]
        maxVal = nums[0]
        for i in range(1, len(nums)):
            if f[i-1] > 0:
                f[i] = nums[i] + f[i-1]
            else:
                f[i] = nums[i]
            if f[i] > maxVal:
                maxVal = f[i]
        return maxVal
