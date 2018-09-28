class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or s is None: return True
        l = len(s)
        start = 0
        end = l - 1
        
        def isValid(c):
            if c.lower().isdigit() or c.lower().isalpha():
                return True
            else:
                return False
        
        while start < end:
            while not isValid(s[start]) and start < l - 1:
                start += 1
            if start == l: 
                break
            
            while not isValid(s[end]) and end > 0:
                end -= 1
                
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                break
            
            
        return end <= start
