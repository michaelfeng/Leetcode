class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        ans = []
        for i in xrange(10):
            self.dfs(A, B, i, ans)
        return sorted(ans)
        
    def dfs(self, n, m, num, ans):
        if num >= n and num <= m:
            ans.append(num)
        if num == 0 or num > m:
            return
        lastDigit = num % 10
        
        stepNumA = num*10 + lastDigit - 1
        stepNumB = num*10 + lastDigit + 1
        
        if lastDigit == 0:
            self.dfs(n, m, stepNumB, ans)
        elif lastDigit == 9:
            self.dfs(n, m, stepNumA, ans)
        else:
            self.dfs(n, m, stepNumA, ans)
            self.dfs(n, m, stepNumB, ans)
        
        
        
if __name__ == '__main__':
    print Solution().stepnum(10,20)
