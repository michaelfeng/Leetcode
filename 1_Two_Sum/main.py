class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = nums
        nums = sorted(nums)
        start, end = 0, len(nums) - 1
        ans = []
        while start < end:
            if nums[start] + nums[end] == target:
                ans.append(nums[start])
                ans.append(nums[end])
                break
            if nums[start] + nums[end] < target:
                start += 1
            if nums[start] + nums[end] > target:
                end -= 1
        
        #print ans
        l = len(nums)
        d = {}
        for i in xrange(l):
            if ans[0] == arr[i]:
                d[i] = i
            if ans[1] == arr[i]:
                d[i] = i
        return sorted([v for k,v in d.items()])
            
                
        
