class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        123
        132
        321
        
        """
        if not nums or len(nums) == 0 or len(nums) == 1: 
            return 0
        nums.append(float('-inf'))
        nums.insert(0, float('-inf'))

        start, end = 1, len(nums) - 2
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            
            if nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        
        print start, end
        if nums[start] < nums[end]:
            return end - 1
        else:
            return start - 1
        
        
            
        
