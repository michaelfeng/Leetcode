class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        ans = [""]*numRows
        index = 0
        while index < len(s):
            # go down
            for i in range(numRows):
                if index < len(s):
                    ans[i] += s[index]
                    index += 1
                    
            # go up
            for i in range(numRows-2, 0, -1):
                if index < len(s):
                    ans[i] += s[index]
                    index += 1
        return ''.join(ans)
