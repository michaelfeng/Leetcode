class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a == 0:
            return 0
        res = 1
        for i in b:
            res = self.modPow(res, 10) * self.modPow(a, i) % 1337
        return res
    
    def modPow(self, x, n):
        ans = 1
        tmp = x
        while n != 0:
            if n % 2 == 1:
                ans *= tmp % 1337
            tmp *= tmp % 1337
            n /= 2
        return ans % 1337
        
