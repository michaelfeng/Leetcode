#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_len = len(height)
        if height_len == 0:
            return 0

        # 找到最大值
        max_index = height.index(max(height))

        # 初始化左边当前最大值
        current_max = 0;

        # 初始化总存水量
        total = 0

        # 爬左楼
        for i in range(max_index):
            if height[i] > current_max:
                # 维护当前最大值
                current_max = height[i]
            else:
                # 累计存水量
                total += current_max - height[i]
            
        # 初始化左边当前最大值
        current_max = height[height_len - 1];
                
        # 爬右楼
        for i in range(max_index, height_len)[::-1]:
            if height[i] > current_max:
                current_max = height[i]
            else:
                total += current_max - height[i]

        return total
                            


if __name__ == '__main__':
    a = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Exptected 6
    print Solution().trap(a)

    a = []
    # Exptected 0
    print Solution().trap(a)
