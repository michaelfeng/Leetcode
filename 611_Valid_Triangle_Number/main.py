class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3: return 0
        nums.sort()
        ans = 0
        for i in xrange(2, len(nums)):
            low, high = 0, i - 1
            while low < high:
                if nums[low] + nums[high] > nums[i]:
                    ans += high - low
                    high -= 1
                else:
                    low += 1
        return ans
