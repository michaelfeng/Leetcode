class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(0,len(p) + 1)] for _ in range(0, len(s) + 1)]
        # print dp
        dp[0][0] = True
        
        for i in range(1, len(p)+1):
            if p[i-1] == "*" and dp[0][i-2]:
                dp[0][i] = True
        
        # print dp
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if p[j-2] != s[i-1] and p[j-2] != '.':
                        # print '#', i, j
                        dp[i][j] = dp[i][j-2]
                    else:
                        # char in p is . or a 
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
                
        return dp[len(s)][len(p)]

