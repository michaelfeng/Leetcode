class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, n, "", res)
        return res

    def dfs(self, left, right, path, res):
        if left > right:
            return  
        if left == 0 and right == 0:
            res.append(path)
            return 
        if left > 0:
            self.dfs(left-1, right, path+"(", res)
        if right > 0:
            self.dfs(left, right-1, path+")", res)
