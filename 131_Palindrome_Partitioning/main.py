class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        self.dfs(s, [], results)
        return results
    
    def dfs(self, s, subsets, results):
        if len(s) == 0:
            results.append(subsets)
            return
        for i in range(1,len(s)+1):
            prefix = s[:i]
            if self.isPalindrome(prefix):
                self.dfs(s[i:], subsets + [prefix], results)
                
    def isPalindrome(self, s):
        return s == s[::-1]
