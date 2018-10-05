class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.check(s[i:j]) or self.check(s[i+1:j+1])
            else:
                i, j = i + 1, j - 1        
        return  True  
    
    def check(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
            else:
                return False
        return True
        
