class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        self.stack = []
        self.ans = 0
        for i in range(len(ops)):
            if ops[i] == 'C':
                self.COP()
            elif ops[i] == 'D':
                self.DOP()
            elif ops[i] == '+':
                self.plus()
            else:
                self.stack.append(int(ops[i]))
                self.ans += int(ops[i])
        return self.ans
    
    def plus(self):
        if len(self.stack) >= 2:
            point= self.stack[-1] + self.stack[-2]
        else:
            point = self.stack[-1]
        self.stack.append(int(point))
        self.ans += int(point)
    
    def COP(self):
        point = self.stack.pop()
        self.ans -= int(point)
        
    def DOP(self):
        point = int(self.stack[-1])*2
        self.stack.append(int(point))
        self.ans += int(point)
        
