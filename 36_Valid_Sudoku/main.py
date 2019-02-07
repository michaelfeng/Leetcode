class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            cols,rows,cubes = {}, {}, {}
            for j in range(n):
                
                if board[i][j] != '.' and board[i][j] in rows: return False
                rows[board[i][j]] = 1
                
                if board[j][i] != '.' and board[j][i] in cols: return False
                cols[board[j][i]] = 1
                
                rowIdx, colIdx = 3*(i/3), 3*(i%3)
                ele = board[rowIdx+j/3][colIdx+j%3]
                if ele != '.' and ele in cubes: return False
                cubes[ele] = 1    
        return True
