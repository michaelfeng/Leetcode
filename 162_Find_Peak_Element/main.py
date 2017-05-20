#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

'''
class Solution(object):
    def findIdx(self, nums, start, end):
        if start == end:
            return start
        if start + 1 == end:
            if nums[start] < nums[end]:
                return end
            else:
                return start
        
        mid = (start + end)/2
        if nums[mid] < nums[mid-1]:
            return self.findIdx(nums, start, mid-1)
        if nums[mid] < nums[mid+1]:
            return self.findIdx(nums, mid, end)
        return mid

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return 0
        return self.findIdx(nums, 0, l - 1)

if __name__ == '__main__':
    nums = [1, 2, 3, 1]

    # Expected: 2
    print Solution().findPeakElement(nums)

    nums = [1, 2, 3, 4, 3]

    # Expected: 3
    print Solution().findPeakElement(nums)
