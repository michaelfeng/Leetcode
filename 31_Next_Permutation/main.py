class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if i >= 1 and nums[i] > nums[i-1]:
                # num[i-1] is the target
                for j in range(len(nums)-1, -1, -1):
                    if j >= i and nums[j] > nums[i-1]:
                        # nums[j] is the number 
                        # which a little bit bigger than nums[i-1]
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        # reverse from i to end(len(nums))
                        start, end = i, len(nums)-1
                        while start <= end:
                            nums[start], nums[end] = nums[end], nums[start]
                            start, end = start+1, end-1
                        return
        nums.reverse()
        return
        
