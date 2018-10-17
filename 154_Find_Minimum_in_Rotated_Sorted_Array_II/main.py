class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            while start+1 < len(nums) and nums[start] <= nums[start+1]:
                start += 1
            while end-1 >= 0 and nums[end] >= nums[end-1]:
                end -= 1
            if nums[start] > nums[end]:
                return nums[end]    

        return nums[start]
        
