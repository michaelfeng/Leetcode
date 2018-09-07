class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        hexs = '0123456789abcdef'
        if num == 0: return "0"
        while num:
            val = num & 0xf
            ans += hexs[val]
            num = num >> 4 if num > 0 else (num + 0x100000000) >> 4
        return ans[::-1]
