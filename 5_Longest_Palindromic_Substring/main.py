class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s or len(s) < 2: return s
        ans = ""
        maxLen = 0
        for i in xrange(len(s)):
            s1, l1 = self.helper(s, i, i)
            s2, l2 = self.helper(s, i, i+1)
            if l1 >= l2 and l1 > maxLen:
                maxLen = l1
                ans = s1
            if l1 <= l2 and l2 > maxLen:
                maxLen = l2
                ans = s2
        return ans
    
    def helper(self, s, left, right):
        while left >= 0 and left < len(s) and right >=0 and right < len(s) and s[left] == s[right]:
            left, right = left-1, right+1
        return s[left+1:right], right-left-1
        
        
            
        
