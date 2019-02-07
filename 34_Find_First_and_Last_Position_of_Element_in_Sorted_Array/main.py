class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0: return [-1,-1]
        left = self.findLeft(nums, target)
        if left == -1: return [-1,-1] 
        return [left, self.findRight(nums, target)]
        
    def findLeft(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo+1 < hi:
            mid = (hi-lo)/2 + lo
            if nums[mid] < target:
                lo = mid
            else:
                hi = mid
        if nums[lo] == target: return lo
        if nums[hi] == target: return hi
        return -1
                
    def findRight(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo+1 < hi:
            mid = (hi-lo)/2 + lo
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid
        if nums[hi] == target: return hi
        if nums[lo] == target: return lo
        return -1
