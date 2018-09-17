class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = 0
        while n:
            res += (n % 10)**2
            n /= 10  
        n = res    
        return self.isHappy(n) if n > 4 else n ==1
        
        
