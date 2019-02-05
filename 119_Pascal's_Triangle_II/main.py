class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1] + [0]*rowIndex
        for i in range(rowIndex):
            for j in range(rowIndex, 0, -1):
                ans[j] = ans[j] + ans[j-1]
        return ans
