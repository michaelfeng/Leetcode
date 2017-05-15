#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return len(word1) + len(word2) - 2 * self.lcs(word1, word2)
                    
    def lcs(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for x in range(len1 + 1)]
        for x in range(len1):
            for y in range(len2):
                dp[x + 1][y + 1] = max(dp[x][y + 1], dp[x + 1][y])
                if word1[x] == word2[y]:
                    dp[x + 1][y + 1] = dp[x][y] + 1
        return dp[len1][len2]
                        
if __name__ == '__main__':
    sol = Solution()
    print sol.minDistance('sea','eat')


'''
最长公共子序列（Longest Common Subsequence）

求word1和word2的LCS

ans = len(word1) + len(word2) - 2 * len(LCS)
'''
