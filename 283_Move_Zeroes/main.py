class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, end = 0, 1, len(nums)
        while i < end and j < end:
            while j < end:
                if nums[j-1] == 0 and nums[j] != 0:
                    break
                j += 1
            if j < end and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
