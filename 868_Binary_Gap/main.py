class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        maxLen = 0
        print s
        for i in range(len(s)-1):
            if s[i] == '1':
                j = i+1
                while j < len(s) and s[j] != '1':
                    j += 1
                if j >= len(s):
                    j = len(s)-1
                    if s[j] != '1':
                        continue 
                maxLen = max(maxLen, j-i)
        return maxLen
