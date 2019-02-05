class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        isFirstRow, isFirstCol = False, False
        m, n = len(matrix), len(matrix[0])
        # Check first col&row contains 0
        for i in range(m):
            if matrix[i][0] == 0:
                isFirstCol = True
        for i in range(n):
            if matrix[0][i] == 0:
                isFirstRow = True
                
        # Update first row&cols which contains 0        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j], matrix[i][0] = 0, 0
        
        # Update element by row
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
                    
        # Update element by col
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
                
        # Update first row
        if isFirstRow:
            for i in range(n):
                matrix[0][i] = 0
        
        # Update first col
        if isFirstCol:
            for i in range(m):
                matrix[i][0] = 0              
        
        
