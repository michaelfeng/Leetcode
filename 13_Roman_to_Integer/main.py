class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        ans = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and d[s[i]] < d[s[i+1]]:
                ans += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans
