class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0: return ""
        s = strs[0]
        l = len(strs)
        for i in xrange(l):
            while strs[i].find(s) != 0:
                s = s[:-1]
        return s
        
