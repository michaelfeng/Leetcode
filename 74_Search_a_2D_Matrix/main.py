class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0: return False
        if len(matrix) == 0 and len(matrix[0]) == 1 and target == matrix[0][0]: return True
        
        n = len(matrix) - 1
        m = len(matrix[0]) - 1

        n_start, m_start = 0, 0
        n_end, m_end = n, m
        n_mid, m_mid = (n_start + n_end)/2, (m_start + m_end)/2

        while n_start <= n_end:
            #print n_start, n_end, n_mid
            if target < matrix[n_mid][0]:
                n_end = n_mid - 1
            elif target > matrix[n_mid][m]:
                n_start = n_mid + 1 
            else:
                while m_start <= m_end:
                    if target < matrix[n_mid][m_start]:
                        return False
                    if target > matrix[n_mid][m_end]:
                        return False
                    if target > matrix[n_mid][m_mid]:
                        m_start = m_mid + 1
                    elif target < matrix[n_mid][m_mid]:
                        m_end = m_mid - 1
                    else:
                        return True
                    m_mid = (m_start + m_end) / 2
            n_mid = (n_start + n_end) / 2    
                
        return False
        
