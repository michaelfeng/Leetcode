class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}

        for c in s:
            counter[c] = counter.get(c, 0) + 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
