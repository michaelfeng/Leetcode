class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4: return []
        nums.sort()
        ans = set()
        for i in xrange(len(nums)-3):
            for j in xrange(i+1, len(nums)-2):
                preSum = nums[i] + nums[j]
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    sufSum = nums[lo] + nums[hi]
                    if preSum + sufSum > target:
                        hi -= 1
                    elif preSum + sufSum < target:
                        lo += 1
                    else:
                        ans.add((nums[i], nums[j], nums[lo], nums[hi]))
                        lo += 1
                    
        return list(ans)
