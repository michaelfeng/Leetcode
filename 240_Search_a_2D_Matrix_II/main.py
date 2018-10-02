class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0: return False

        
        n = len(matrix) - 1
        m = len(matrix[0]) - 1
        i = 0
        y = m
        while i <= n:
            while y >= 0 and matrix[i][y] > target:
                y -= 1
            if y >= 0 and matrix[i][y] == target: 
                return True
            i += 1
                
        return False
