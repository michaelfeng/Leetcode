class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0: return -1
        if len(nums) == 1:
            if target == nums[0]: 
                return 0
            else:
                return -1
            
        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2 
        while start <= end:
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
            mid = (start + end) / 2
            
        return -1
