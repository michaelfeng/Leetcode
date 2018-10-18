class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n > 26:
            num = n % 26
            n = n / 26
            if num == 0:
                ans = "Z" + ans
                n -= 1
                continue
            char = chr(num+64)
            ans = char + ans
            
        ans = chr(n+64) + ans
        return ans
