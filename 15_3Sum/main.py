class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3: return []
        nums.sort()
        ans = set()
        for i in xrange(len(nums)):
            low, high = i + 1, len(nums) - 1
            while low < high:
                target = 0 - nums[i]
                if nums[low] + nums[high] == target:
                    ans.add((nums[i], nums[low], nums[high]))
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1            
        return list(ans)    
        
        
