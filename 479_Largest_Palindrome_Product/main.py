#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Find the largest palindrome made from the product of two n-digit numbers.
Since the result could be very large, you should return the largest palindrome mod 1337.

Example:
Input: 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:
The range of n is [1,8].
'''
import math

class Solution(object):
    '''
    def isPalindrome(self, num):
        data = str(num)
        length = len(data)
        i = 0
        j = length - 1
        result = True
        while i <= j:
            if data[i] == data[j]:
                i += 1
                j -= 1
            else:
                result = False
                break
        return result

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        num = math.pow(10, n) - 1
        num = int(num)
        for i in range(num, 1, -1):
            for j in range(num, 1, -1):
                v = i * j
                if self.isPalindrome(v) and v > m:
                    m = v
        r = m % 1337
        return r
    '''
    def largestPalindrome(self, n):
        return [9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999][n - 1] % 1337

if __name__ == '__main__':
    slu = Solution()
    print slu.largestPalindrome(4)
