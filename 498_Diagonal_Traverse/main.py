class Solution:
    """
    @param matrix: a 2D array
    @return: return a list of integers
    """
    def findDiagonalOrder(self, matrix):
        # write your code here
        if not matrix: return []
        if len(matrix) == 0: return []
        if len(matrix[0]) == 0: return []
        
        n = len(matrix)
        m = len(matrix[0])
        
        x, y = 0, 0
        dx, dy = -1, 1
        ans = []
        while not (x == n - 1 and y == m - 1):
            ans.append(matrix[x][y])
            # in matrix
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                x, y = nx, ny
            else:
                if dx == -1:
                    if ny == m:
                        x, y = x + 1, y
                    else:
                        x, y = x, y + 1
                else:
                    if nx == n:
                        x, y = x, y + 1
                    else:
                        x, y = x + 1, y
                dx *= -1
                dy *= -1
                
        ans.append(matrix[n-1][m-1])        
        return ans
