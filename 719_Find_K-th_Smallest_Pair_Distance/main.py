import heapq
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        # lo is least difference 
        # hi is maximun difference
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo+hi)//2
            if self.countPair(nums, mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def countPair(self, nums, diffVal):
        left, right, ans = 0, 0, 0
        while right != len(nums):
            while nums[right] - nums[left] > diffVal:
                left += 1
            ans += right - left
            right += 1
        return ans
        
        
        
            
