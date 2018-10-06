class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0: return None
        index = self.partition(nums, 0, 0)
        self.partition(nums, index, 1)
    
    def partition(self, nums, l, pivot):
        start, end = l, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] == pivot:
                start += 1
            while start <= end and nums[end] != pivot:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start+1, end-1
        return start
        
        
