class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, res, 0, [])
        return res
    
    def dfs(self, s, res, startInd, subset):
        if len(subset) == 4 and startInd == len(s):
            res.append('.'.join(subset))
            return
        
        for i in range(startInd, startInd + 3):
            if i >= len(s):
                return
            substring = s[startInd : i + 1]
            num = int(substring)
            if num < 0 or num > 255 or len(substring) != len(str(num)):
                continue
            subset.append(substring)
            self.dfs(s, res, i+1, subset)
            subset.pop()
        
