class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0: return s
        l = len(s)
        dp = [[False] * l for i in range(l)]
        #print l
        ans = ""
        maxLen = 0
        for j in range(0, l):
            for i in range(0, j+1):
                dp[i][j] = (s[i] == s[j]) and ((j - i <= 2) or dp[i+1][j-1])
                #print i, j, s[i],s[j],j - i
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    ans = s[i:j+1]
        return ans
