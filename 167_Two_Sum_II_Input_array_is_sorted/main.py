class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            elif nums[lo] + nums[hi] < target:
                lo += 1
            else:
                return [lo+1, hi+1]
        return [] 
