#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        min = sys.maxint
        res = 0
        for i in range(n):
            l = i + 1; r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                distance = math.fabs(sum - target)
                if distance < min:
                    min = distance
                    res = sum
                if sum == target:
                    return sum
                if sum < target:
                    l += 1
                if sum > target:
                    r -= 1
            
        return res
                            


if __name__ == '__main__':
    a = [-1,2,1,-4]

    # Expected 2
    print "Three sum closest: ", Solution().threeSumClosest(a, 1) 

    b = [1,1,1,0]
    # Expected 2
    print "Three sum closest: ", Solution().threeSumClosest(b, -100) 


# 双标法
