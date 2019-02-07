class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        arr = []
        while x:
            arr.append(x % 10)
            x /= 10
        return arr[::-1] == arr
        
