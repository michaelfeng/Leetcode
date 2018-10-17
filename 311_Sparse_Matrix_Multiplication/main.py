class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        n = len(A)
        m = len(A[0])
        k = len(B[0])

        C = [[0 for _ in xrange(k)] for i in xrange(n)]

        for i in xrange(n):
            for j in xrange(m):
                if A[i][j] != 0:
                    for l in xrange(k):
                        C[i][l] += A[i][j] * B[j][l]
        return C
