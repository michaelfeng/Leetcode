#!/bin/python

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        # print row, col
        
        ans = [x[:] for x in [[0] * row] * col] 
        for i in range(row):
            for j in range(col):
                ans[j][i] = A[i][j]
        # print ans
        return ans
        
        
