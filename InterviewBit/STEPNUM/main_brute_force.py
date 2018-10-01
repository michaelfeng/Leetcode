class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        ans = []
        for i in xrange(A, B+1):
            if self.isSteppingNum(i):
                ans.append(i)
        return ans
        
    def isSteppingNum(self, num):
        pre = num % 10
        num = num / 10
        while num > 0:
            cur = num % 10
            if abs(cur - pre) != 1:
                return False
            pre = cur
            num = num / 10
        return True
        
