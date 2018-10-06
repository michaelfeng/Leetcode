class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3: return 0
        ans = nums[0] + nums[1] + nums[len(nums)-1] 
        nums.sort()
        for i in xrange(len(nums)-2):
            lo, hi = i+1, len(nums) - 1
            while lo < hi:
                sumVal = nums[i] + nums[lo] + nums[hi]
                if sumVal > target:
                    hi -= 1
                else:
                    lo += 1
                if abs(sumVal - target) < abs(ans - target):
                    ans = sumVal
        return ans
        
