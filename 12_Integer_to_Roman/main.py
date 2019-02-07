class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roms = ["M", "CM","D", "CD", "C", "XC", "L", "XL", "X", "IX", "V","IV", "I"]
        ans = ""
        for i in range(len(arr)):
            while num >= arr[i]:
                num -= arr[i]
                ans += roms[i]
        return ans
                
        
